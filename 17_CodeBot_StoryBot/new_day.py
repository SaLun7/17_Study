"""Create a DAY notebook without overwriting existing work."""
import argparse
import json
from pathlib import Path
from uuid import uuid4

ROOT = Path(__file__).resolve().parent
KERNEL_NAME = "codebot-storybot"


def cell(kind, source):
    result = {"cell_type": kind, "id": uuid4().hex[:8], "metadata": {}, "source": source.splitlines(True)}
    if kind == "code":
        result.update(execution_count=None, outputs=[])
    return result


def create_notebook(folder, title):
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "01.ipynb"
    if target.exists() and target.stat().st_size:
        raise FileExistsError(f"Existing notebook preserved: {target}")
    notebook = {
        "cells": [
            cell("markdown", f"# {title}\n\n커널: **Python (CodeBot StoryBot CUDA)**\n\n아래 셀로 가상환경과 GPU를 확인하세요."),
            cell("code", "import sys\nimport torch\n\nprint('Python:', sys.executable)\nprint('PyTorch:', torch.__version__)\nprint('CUDA:', torch.version.cuda)\nassert torch.cuda.is_available(), '프로젝트의 CUDA 커널을 선택하세요.'\ndevice = torch.device('cuda')\nprint('GPU:', torch.cuda.get_device_name(0))\nx = torch.randn(256, 256, device=device, requires_grad=True)\nloss = (x @ x.T).square().mean()\nloss.backward()\ntorch.cuda.synchronize()\nprint('GPU 연산 성공:', loss.item())"),
            cell("markdown", "## 학습 내용\n\n오늘 학습할 내용을 기록하세요."),
            cell("code", ""),
        ],
        "metadata": {
            "kernelspec": {"display_name": "Python (CodeBot StoryBot CUDA)", "language": "python", "name": KERNEL_NAME},
            "language_info": {"name": "python", "version": "3.12.14"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    target.write_text(json.dumps(notebook, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(target)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("day", type=int, help="Day number, e.g. 2")
    args = parser.parse_args()
    if args.day < 1:
        parser.error("day must be at least 1")
    create_notebook(ROOT / f"DAY{args.day}", f"DAY {args.day}")
