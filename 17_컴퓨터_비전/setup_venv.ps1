[CmdletBinding()]
param(
    [switch]$Recreate,
    [switch]$Full
)

$ErrorActionPreference = 'Stop'
$projectRoot = $PSScriptRoot
$venvPath = Join-Path $projectRoot '.venv'

function Find-Python310 {
    $candidates = @(
        (Join-Path $env:LOCALAPPDATA 'Programs\Python\Python310\python.exe'),
        (Join-Path $env:ProgramFiles 'Python310\python.exe')
    )

    $launcher = Get-Command py -ErrorAction SilentlyContinue
    if ($launcher) {
        try {
            $path = & $launcher.Source -3.10 -c 'import sys; print(sys.executable)'
            if ($LASTEXITCODE -eq 0 -and (Test-Path -LiteralPath $path)) { return $path }
        } catch {}
    }

    foreach ($candidate in $candidates) {
        if ($candidate -and (Test-Path -LiteralPath $candidate)) { return $candidate }
    }

    throw 'Python 3.10을 찾지 못했습니다. Python 3.10 (64-bit)을 설치한 뒤 다시 실행하세요: https://www.python.org/downloads/release/python-31011/'
}

$python = Find-Python310
$version = & $python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")'
if ($version -ne '3.10') { throw "Python 3.10이 필요하지만 $version을 찾았습니다." }

if ($Recreate -and (Test-Path -LiteralPath $venvPath)) {
    $resolvedVenv = (Resolve-Path -LiteralPath $venvPath).Path
    if ($resolvedVenv -ne (Join-Path $projectRoot '.venv')) { throw "삭제 대상이 올바르지 않습니다: $resolvedVenv" }
    Remove-Item -LiteralPath $resolvedVenv -Recurse -Force
}

if (-not (Test-Path -LiteralPath (Join-Path $venvPath 'Scripts\python.exe'))) {
    & $python -m venv $venvPath
}

$venvPython = Join-Path $venvPath 'Scripts\python.exe'
& $venvPython -m pip install --upgrade pip wheel setuptools

if ($Full) {
    & $venvPython -m pip install -r (Join-Path $projectRoot 'requirements.txt')
} else {
    & $venvPython -m pip install tensorflow==2.15.0 pillow==9.4.0 opencv-python==4.8.0.76 tensorflow-hub==0.16.1 tensorflow-probability==0.23.0 tensorflow-datasets==4.9.4 tensorflow-metadata==1.14.0 'setuptools<81' numpy pandas matplotlib seaborn scikit-learn scikit-image tqdm imageio xmltodict jupyterlab notebook ipykernel
}

# DAY4 4_4 및 5 노트북 의존성. tfswin 4.x는 Keras 3 전용이므로 3.4로 고정한다.
& $venvPython -m pip install tfswin==3.4.0 tf-slim pycocotools

$modelsResearch = Join-Path $projectRoot 'models\research'
if (Test-Path -LiteralPath (Join-Path $modelsResearch 'object_detection')) {
    & $venvPython -m pip install grpcio-tools==1.48.2 --no-deps
    & $venvPython -c 'import os, site; p=os.path.join(site.getsitepackages()[-1], "computer_vision_models.pth"); open(p, "w", encoding="ascii").write("../../../models/research\n../../../models/research/slim\nimport object_detection.protos, os, sys; object_detection.protos.__path__.append(os.path.join(sys.prefix, ''object_detection'', ''protos''))\n")'
    & $venvPython -c 'import os, sys; from grpc_tools import protoc; root=sys.argv[1]; proto=os.path.join(root, "object_detection", "protos", "string_int_label_map.proto"); raise SystemExit(protoc.main(["protoc", "--proto_path="+root, "--python_out="+sys.prefix, proto]))' $modelsResearch
} else {
    Write-Warning 'models 서브모듈이 없습니다. git submodule update --init --recursive 실행 후 다시 설정하세요.'
}

& $venvPython -m ipykernel install --user --name computer-vision --display-name 'Python (컴퓨터 비전)'
& $venvPython -c 'import cv2, tensorflow as tf, tfswin; print("가상환경 준비 완료"); print("OpenCV", cv2.__version__); print("TensorFlow", tf.__version__); print("tfswin", tfswin.__version__)'

Write-Host "활성화: .\.venv\Scripts\Activate.ps1"
Write-Host 'JupyterLab 실행: jupyter lab'
