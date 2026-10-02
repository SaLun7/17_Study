"""Project-local Jupyter startup compatibility for Windows.

Loading PyTorch before pyarrow avoids a Windows DLL initialization conflict.
This directory is added only to the Vision Transformer Jupyter kernel.
"""

import torch  # noqa: F401
