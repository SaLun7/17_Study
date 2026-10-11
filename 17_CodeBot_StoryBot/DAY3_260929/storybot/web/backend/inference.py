"""Adapter around the existing StoryBot model, tokenizer, and generate function."""

import sys
from pathlib import Path
from threading import Lock


STORYBOT_DIR = Path(__file__).resolve().parents[2]
if str(STORYBOT_DIR) not in sys.path:
    sys.path.insert(0, str(STORYBOT_DIR))

from model import GPT  # noqa: E402
from tokenizer import BPETokenizer  # noqa: E402
from utils import generate, get_device  # noqa: E402


MAX_INPUT_TOKENS = 56
MAX_NEW_TOKENS = 200
CONTEXT_LENGTH = 256


class StoryEngine:
    def __init__(self):
        self._lock = Lock()  # The existing model mutates its KV cache per request.
        self.tokenizer = BPETokenizer.load_from(STORYBOT_DIR / "merge_rules.pkl")
        self.model = GPT.load_from(STORYBOT_DIR / "model_pretrain.pt", device=get_device())
        self.model.eval()
        if self.model.max_context_len != CONTEXT_LENGTH:
            raise RuntimeError("스토리봇 모델의 문맥 길이가 예상한 256토큰과 다릅니다.")
        if self.model.vocab_size != self.tokenizer.vocab_size:
            raise RuntimeError("스토리봇 모델과 토크나이저의 어휘 크기가 다릅니다.")

    def token_count(self, prompt: str) -> int:
        return len(self.tokenizer.encode(prompt))

    def complete(self, prompt: str) -> str:
        with self._lock:
            return generate(
                self.model,
                self.tokenizer,
                prompt,
                max_new_tokens=MAX_NEW_TOKENS,
                temperature=1.0,
            )


_engine = None
_engine_lock = Lock()


def get_engine() -> StoryEngine:
    global _engine
    if _engine is None:
        with _engine_lock:
            if _engine is None:
                _engine = StoryEngine()
    return _engine
