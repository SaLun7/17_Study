$ErrorActionPreference = "Stop"

$ProjectRoot = $PSScriptRoot
$VenvRoot = if ($env:NLP_CV_VENV) {
    [Environment]::ExpandEnvironmentVariables($env:NLP_CV_VENV)
}
else {
    Join-Path $env:USERPROFILE ".venvs\nlp-cv"
}
$VenvPython = Join-Path $VenvRoot "Scripts\python.exe"

if (-not (Test-Path -LiteralPath $VenvPython)) {
    $PyLauncher = Get-Command py -ErrorAction SilentlyContinue
    if ($PyLauncher) {
        & $PyLauncher.Source -3.12 -m venv $VenvRoot
    }
    else {
        $PythonCommand = Get-Command python -ErrorAction SilentlyContinue
        if (-not $PythonCommand) {
            throw "Python 3.12를 찾지 못했습니다. Python 3.12를 설치한 뒤 다시 실행해 주세요."
        }
        $PythonVersion = & $PythonCommand.Source -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"
        if ($PythonVersion -ne "3.12") {
            throw "Python 3.12가 필요하지만 현재 python은 $PythonVersion 입니다."
        }
        & $PythonCommand.Source -m venv $VenvRoot
    }
}

& $VenvPython -m pip install --upgrade pip setuptools wheel
& $VenvPython -m pip install -r (Join-Path $ProjectRoot "requirements-cuda.txt")
& $VenvPython -m pip install -r (Join-Path $ProjectRoot "requirements-windows.txt")
$KernelArguments = @(
    "--user",
    "--name", "nlp-cv-gpu-ascii",
    "--display-name", "Python (NLP-CV GPU ASCII)"
)
if ($env:JAVA_HOME) {
    $KernelArguments += @("--env", "JAVA_HOME", $env:JAVA_HOME)
}
& $VenvPython -m ipykernel install @KernelArguments
& $VenvPython (Join-Path $ProjectRoot "verify_gpu.py")
