@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\horizon-wizard.exe" (
  echo Horizon runtime is missing. Please reinstall dependencies first.
  pause
  exit /b 1
)

echo Starting Horizon setup wizard...
echo Your configuration will be saved to data\config.json.
echo.
".venv\Scripts\horizon-wizard.exe"
set "HORIZON_EXIT=%ERRORLEVEL%"
echo.
if not "%HORIZON_EXIT%"=="0" echo Setup exited with code %HORIZON_EXIT%.
pause
exit /b %HORIZON_EXIT%
