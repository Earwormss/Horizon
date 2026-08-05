@echo off
setlocal
cd /d "%~dp0"

if not exist "data\config.json" (
  echo Horizon has not been configured yet.
  echo Run setup-horizon.cmd first.
  pause
  exit /b 1
)

if not exist ".venv\Scripts\horizon.exe" (
  echo Horizon runtime is missing. Please reinstall dependencies first.
  pause
  exit /b 1
)

echo Running Horizon for the last 24 hours...
".venv\Scripts\horizon.exe" --hours 24
set "HORIZON_EXIT=%ERRORLEVEL%"
echo.
if "%HORIZON_EXIT%"=="0" (
  echo Finished. Reports are under data\summaries.
) else (
  echo Horizon exited with code %HORIZON_EXIT%.
)
pause
exit /b %HORIZON_EXIT%
