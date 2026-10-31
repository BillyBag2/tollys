@echo off
setlocal
python "%~dp0menu\build_menu.py"
if errorlevel 1 (
    echo.
    echo The menu could not be created. Check that Python 3.10 or newer is installed and review the error above.
    pause
    exit /b 1
)
endlocal
