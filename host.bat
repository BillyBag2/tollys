@echo off
setlocal
echo Open Tolly's Cafe in your browser:
echo http://localhost:8000
echo.
echo Press Ctrl+C to stop the server.
echo.
python -m http.server 8000 --bind 127.0.0.1 --directory "%~dp0docs"
if errorlevel 1 (
    echo.
    echo The server could not start. Check that Python is installed and port 8000 is available.
    pause
)
endlocal
