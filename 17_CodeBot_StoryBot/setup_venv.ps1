param([string]$Python = "python")
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (-not (Test-Path ".venv/Scripts/python.exe")) {
    & $Python -m venv .venv
    if ($LASTEXITCODE -ne 0) { throw "Virtual environment creation failed. Use Python 3.12." }
}
$venvPython = Join-Path $PSScriptRoot ".venv/Scripts/python.exe"
& $venvPython -m pip install -r requirements-cuda.txt
if ($LASTEXITCODE -ne 0) { throw "Dependency installation failed." }
& $venvPython -m ipykernel install --sys-prefix --name codebot-storybot --display-name "Python (CodeBot StoryBot CUDA)" --env IPYTHONDIR (Join-Path $PSScriptRoot ".venv/.ipython")
if ($LASTEXITCODE -ne 0) { throw "Kernel installation failed." }
& $venvPython -m pip check
if ($LASTEXITCODE -ne 0) { throw "Dependency compatibility check failed." }
& $venvPython verify_cuda.py
if ($LASTEXITCODE -ne 0) { throw "CUDA validation failed." }

