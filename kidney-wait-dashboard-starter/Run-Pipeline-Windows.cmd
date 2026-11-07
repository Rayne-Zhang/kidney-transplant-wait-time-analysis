@echo off
cd /d "%~dp0"
py -m kidney_wait.pipeline
if errorlevel 1 (
  echo Pipeline failed. Ensure Python 3.10+ is installed.
) else (
  echo Outputs generated in build\.
)
pause
