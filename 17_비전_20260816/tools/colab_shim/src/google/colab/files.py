"""Local substitutes for the basic ``google.colab.files`` helpers."""

from pathlib import Path
from typing import Iterable


def upload() -> dict[str, bytes]:
    raise RuntimeError(
        "files.upload() requires Colab's browser UI. Copy the file into the "
        "project directory and open it with pathlib.Path instead."
    )


def download(filename: str) -> Path:
    path = Path(filename).resolve()
    if not path.is_file():
        raise FileNotFoundError(path)
    return path


def view(filename: str) -> Path:
    return download(filename)

