@echo off
setlocal EnableExtensions
cd /d "%~dp0"

echo ========================================
echo Horizon portable installer for Windows
echo ========================================
echo.

set "UV_EXE=uv"
where uv >nul 2>nul
if errorlevel 1 (
  if exist "%USERPROFILE%\.local\bin\uv.exe" (
    set "UV_EXE=%USERPROFILE%\.local\bin\uv.exe"
  ) else (
    echo uv was not found. Installing it now...
    powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "irm https://astral.sh/uv/install.ps1 | iex"
    if errorlevel 1 goto :install_failed
    if exist "%USERPROFILE%\.local\bin\uv.exe" (
      set "UV_EXE=%USERPROFILE%\.local\bin\uv.exe"
    ) else (
      echo uv was installed, but this window cannot find it yet.
      echo Close this window and run install-horizon.cmd again.
      pause
      exit /b 1
    )
  )
)

echo Creating the Python 3.12 environment...
"%UV_EXE%" venv --python 3.12 .venv
if errorlevel 1 goto :install_failed

echo Installing Horizon and its dependencies...
"%UV_EXE%" pip install --python ".venv\Scripts\python.exe" -e .
if errorlevel 1 goto :install_failed

if not exist "data\config.json" (
  copy /Y "data\config.local.example.json" "data\config.json" >nul
  echo Created data\config.json from today's portable settings.
) else (
  echo Keeping your existing data\config.json.
)

if not exist ".env" (
  copy /Y ".env.example" ".env" >nul
  echo Created .env. Add your DEEPSEEK_API_KEY before running Horizon.
) else (
  echo Keeping your existing .env.
)

echo.
echo Installation finished.
echo 1. Open .env and set DEEPSEEK_API_KEY.
echo 2. Double-click run-horizon.cmd.
echo 3. Reports will appear under data\summaries.
pause
exit /b 0

:install_failed
echo.
echo Installation failed with code %ERRORLEVEL%.
pause
exit /b 1
