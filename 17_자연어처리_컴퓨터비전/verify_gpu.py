import sys

import torch


print(f"Python: {sys.version.split()[0]}")
print(f"PyTorch: {torch.__version__}")
print(f"PyTorch CUDA runtime: {torch.version.cuda}")
print(f"CUDA available: {torch.cuda.is_available()}")

if not torch.cuda.is_available():
    raise SystemExit("CUDA GPU를 사용할 수 없습니다.")

device = torch.device("cuda")
x = torch.randn(1024, 1024, device=device)
y = x @ x
torch.cuda.synchronize()

print(f"GPU: {torch.cuda.get_device_name(0)}")
print(f"Compute capability: {torch.cuda.get_device_capability(0)}")
print(f"GPU tensor test: OK ({y.device})")
