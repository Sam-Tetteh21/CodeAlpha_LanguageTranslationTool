@echo off
setlocal
cd /d "%~dp0"

echo Setting up Language Translation Tool...

if not exist ".venv\Scripts\python.exe" (
    echo Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 goto :error
)

echo Installing dependencies...
.venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 goto :error

echo Starting the app...
.venv\Scripts\python.exe -m streamlit run app.py
if errorlevel 1 goto :error

goto :eof

:error
echo.
echo The app could not be started. Make sure Python is installed and available on PATH.
pause
exit /b 1
