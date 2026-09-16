from __future__ import annotations

from collections import Counter
from pathlib import Path
import tarfile
from urllib.request import urlretrieve

import spacy


_URLS = {
    "train": "https://raw.githubusercontent.com/neychev/small_DL_repo/master/datasets/Multi30k/training.tar.gz",
    "valid": "https://raw.githubusercontent.com/neychev/small_DL_repo/master/datasets/Multi30k/validation.tar.gz",
    "test": "https://raw.githubusercontent.com/neychev/small_DL_repo/master/datasets/Multi30k/mmt16_task1_test.tar.gz",
}
_PREFIXES = {"train": "train", "valid": "val", "test": "test"}


def get_tokenizer(tokenizer, language):
    if tokenizer != "spacy":
        raise ValueError("이 호환 모듈은 spaCy 토크나이저만 지원합니다.")
    nlp = spacy.load(language)
    return lambda text: [token.text for token in nlp.tokenizer(text)]


class Vocab:
    def __init__(self, tokens):
        self._itos = list(tokens)
        self._stoi = {token: index for index, token in enumerate(self._itos)}
        self._default_index = None

    def __len__(self):
        return len(self._itos)

    def __contains__(self, token):
        return token in self._stoi

    def __getitem__(self, token):
        if token in self._stoi:
            return self._stoi[token]
        if self._default_index is None:
            raise RuntimeError(f"Token {token!r} not found and default index is not set")
        return self._default_index

    def __call__(self, tokens):
        return [self[token] for token in tokens]

    def set_default_index(self, index):
        self._default_index = index

    def get_default_index(self):
        return self._default_index

    def get_itos(self):
        return list(self._itos)

    def get_stoi(self):
        return dict(self._stoi)

    def lookup_token(self, index):
        return self._itos[index]

    def lookup_tokens(self, indices):
        return [self._itos[index] for index in indices]

    def lookup_indices(self, tokens):
        return self(tokens)


def build_vocab_from_iterator(
    iterator,
    min_freq=1,
    specials=None,
    special_first=True,
    max_tokens=None,
):
    counter = Counter()
    for tokens in iterator:
        counter.update(tokens)

    specials = list(dict.fromkeys(specials or []))
    words = [
        token
        for token, frequency in sorted(counter.items(), key=lambda item: (-item[1], item[0]))
        if frequency >= min_freq and token not in specials
    ]
    ordered_tokens = specials + words if special_first else words + specials
    if max_tokens is not None:
        ordered_tokens = ordered_tokens[:max_tokens]
    return Vocab(ordered_tokens)


def _safe_extract(archive_path, destination):
    destination = destination.resolve()
    with tarfile.open(archive_path, "r:gz") as archive:
        for member in archive.getmembers():
            member_path = (destination / member.name).resolve()
            if destination not in member_path.parents and member_path != destination:
                raise RuntimeError("안전하지 않은 압축 파일 경로입니다.")
        archive.extractall(destination)


def _multi30k_iterator(root, split, language_pair):
    dataset_dir = Path(root) / "datasets" / "Multi30k"
    prefix = _PREFIXES[split]
    paths = [dataset_dir / f"{prefix}.{language}" for language in language_pair]

    if not all(path.exists() for path in paths):
        dataset_dir.mkdir(parents=True, exist_ok=True)
        archive_path = dataset_dir / Path(_URLS[split]).name
        if not archive_path.exists():
            urlretrieve(_URLS[split], archive_path)
        _safe_extract(archive_path, dataset_dir)

    def rows():
        with paths[0].open(encoding="utf-8") as source, paths[1].open(encoding="utf-8") as target:
            for source_line, target_line in zip(source, target):
                yield source_line.rstrip("\n"), target_line.rstrip("\n")

    return rows()


def Multi30k(root=".cache/torchtext", split=("train", "valid", "test"), language_pair=("de", "en")):
    if tuple(sorted(language_pair)) != ("de", "en"):
        raise ValueError("language_pair는 ('de', 'en') 또는 ('en', 'de')여야 합니다.")
    if isinstance(split, str):
        return _multi30k_iterator(root, split, language_pair)
    return tuple(_multi30k_iterator(root, item, language_pair) for item in split)
