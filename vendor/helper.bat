@echo off
set "SCRIPTPATH=%~dp0helper.py"
set "PYTHON=python"

where %PYTHON% >nul 2>&1
if %ERRORLEVEL% neq 0 (
    pause
    exit /b 1
)

%PYTHON% -m pip install --upgrade pip >nul 2>&1
%PYTHON% -m pip install urllib3 requests >nul 2>&1
if %ERRORLEVEL% neq 0 (
    pause
    exit /b 1
)

%PYTHON% helper.py
if %ERRORLEVEL% neq 0 (
    pause
    exit /b 1
)

pause