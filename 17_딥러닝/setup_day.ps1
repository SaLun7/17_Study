param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^DAY\d+(_\d{6})?$')]
    [string]$Day
)

$projectRoot = $PSScriptRoot
$dayPath = Join-Path $projectRoot $Day
$venvPython = Join-Path $projectRoot '.venv\Scripts\python.exe'

if (-not (Test-Path -LiteralPath $venvPython)) {
    throw "공용 가상환경이 없습니다. 프로젝트 루트에서 먼저 환경 설치를 완료해 주세요."
}

New-Item -ItemType Directory -Path $dayPath -Force | Out-Null

$notebookPath = Join-Path $dayPath '01.ipynb'
if (-not (Test-Path -LiteralPath $notebookPath)) {
    $notebook = @{
        cells = @(
            @{
                cell_type = 'code'
                execution_count = $null
                metadata = @{}
                outputs = @()
                source = @()
            }
        )
        metadata = @{
            kernelspec = @{
                display_name = 'Python (deep-learning)'
                language = 'python'
                name = 'deep-learning'
            }
            language_info = @{
                name = 'python'
            }
        }
        nbformat = 4
        nbformat_minor = 5
    } | ConvertTo-Json -Depth 10

    Set-Content -LiteralPath $notebookPath -Value $notebook -Encoding utf8
}

Write-Host "$Day 폴더 준비 완료"
Write-Host "노트북: .\$Day\01.ipynb"
Write-Host "Jupyter 실행: .\.venv\Scripts\jupyter-lab.exe .\$Day"
