param(
    [string]$Day = 'DAY1_260901'
)

$projectRoot = $PSScriptRoot
$dayPath = Join-Path $projectRoot $Day
$jupyter = Join-Path $projectRoot '.venv\Scripts\jupyter-lab.exe'

if (-not (Test-Path -LiteralPath $dayPath)) {
    throw "폴더를 찾을 수 없습니다: $Day (먼저 .\setup_day.ps1 -Day $Day 실행)"
}
if (-not (Test-Path -LiteralPath $jupyter)) {
    throw "Jupyter 환경이 없습니다. requirements 설치를 먼저 완료해 주세요."
}

& $jupyter $dayPath
