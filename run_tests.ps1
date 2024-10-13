# run_tests.ps1

param (
    [string]$Test = ""
)

# 設置 PYTHONPATH
$env:PYTHONPATH = "../src"

# 如果指定了測試文件，則運行該文件；否則運行全部測試
if ($Test -ne "") {
    Write-Host "Running single test: $Test"
    python -m unittest tests/$Test
} else {
    Write-Host "Running all tests"
    python -m unittest discover -s tests
}
