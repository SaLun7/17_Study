"""Check package compatibility and perform a real CUDA forward/backward pass."""
import sys

import matplotlib
import numpy as np
import openai
import regex
import tiktoken
import torch
import tqdm
import wandb


def main():
    print("Python:", sys.version.split()[0])
    print("Executable:", sys.executable)
    print("PyTorch:", torch.__version__)
    print("NumPy:", np.__version__)
    print("CUDA runtime:", torch.version.cuda)
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA unavailable. Select this project's .venv kernel.")
    print("GPU:", torch.cuda.get_device_name(0))
    print("Compute capability:", torch.cuda.get_device_capability(0))
    x = torch.randn(256, 256, device="cuda", requires_grad=True)
    loss = (x @ x.T).square().mean()
    loss.backward()
    torch.cuda.synchronize()
    assert x.grad is not None and torch.isfinite(x.grad).all().item()
    np.testing.assert_array_equal(torch.from_numpy(np.arange(5)).numpy(), np.arange(5))
    print("PASS: required imports, NumPy bridge, CUDA matrix multiplication and backward")


if __name__ == "__main__":
    main()
