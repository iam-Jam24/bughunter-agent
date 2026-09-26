# Restore shopkart-api to the buggy demo baseline so Bug Hunter can be demoed again.
# Usage: .\scripts\reset_target.ps1 [-Path <local clone of shopkart-api>]
param([string]$Path = (Join-Path $PSScriptRoot "..\..\shopkart-api"))

$ErrorActionPreference = "Stop"
Set-Location $Path

git checkout main
git pull --tags origin main
git checkout demo-baseline -- .

if (git status --porcelain) {
    git commit -am "Reset to demo baseline"
    git push origin main
    Write-Host "shopkart-api reset to demo-baseline. Close leftover issues and PRs on GitHub."
} else {
    Write-Host "shopkart-api already matches demo-baseline."
}
