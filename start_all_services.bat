@echo off
REM iSipnayan Full System Launcher
REM Starts Backend API, Media Server, and optionally the Frontend

setlocal enabledelayedexpansion

echo.
echo ================================================
echo   iSipnayan Full System Startup
echo ================================================
echo.

REM Kill any existing Node.js and Python processes to free ports
echo [0/4] Cleaning up existing processes...
echo.
echo Stopping existing services on ports 3001, 5000, 5173...
taskkill /F /IM node.exe >nul 2>&1
taskkill /F /IM python.exe >nul 2>&1
timeout /t 2 /nobreak >nul

REM Get current directory
set SCRIPT_DIR=%~dp0
set BACKEND_DIR=%SCRIPT_DIR%backend
set MEDIA_SERVER_DIR=%SCRIPT_DIR%media_server
set FRONTEND_DIR=%SCRIPT_DIR%

REM Color codes (Windows doesn't support colored output natively)
REM We'll use different approaches

echo [1/5] Checking prerequisites...

REM Check Node.js
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed
    echo Please install Node.js from https://nodejs.org/
    pause
    exit /b 1
)
echo ✓ Node.js found: 
node --version

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed
    echo Please install Python 3.7+ from https://python.org/
    pause
    exit /b 1
)
echo ✓ Python found:
python --version

echo.
echo [2/5] Starting Media Server (Python Flask)...
echo.
cd /d "%MEDIA_SERVER_DIR%"
if not exist "venv" (
    echo Creating Python virtual environment...
    python -m venv venv
)
call venv\Scripts\activate.bat
pip install -r requirements.txt >nul 2>&1

REM Start media server in background
echo Starting on http://localhost:5000...
start "iSipnayan Media Server" python app.py

REM Give media server time to start
timeout /t 3 /nobreak

echo.
echo [3/5] Starting Backend API (Node.js)...
echo.
cd /d "%BACKEND_DIR%"
if not exist "node_modules" (
    echo Installing dependencies...
    call npm install
)

echo Starting on http://localhost:3001...
start "iSipnayan Backend API" cmd /k "npm run dev"

REM Give backend time to start
timeout /t 2 /nobreak

echo.
echo [4/5] Starting Frontend (React/Vite)...
echo.
cd /d "%FRONTEND_DIR%"
if not exist "node_modules" (
    echo Installing dependencies...
    call npm install
)

echo Starting on http://localhost:5173...
start "iSipnayan Frontend" cmd /k "npm run dev"

timeout /t 2 /nobreak

echo.
echo [5/5] Setup Complete!
echo.
echo ================================================
echo   System Status
echo ================================================
echo.
echo   Frontend:      http://localhost:5173
echo   Backend API:   http://localhost:3001
echo   Media Server:  http://localhost:5000
echo.
echo   ✓ All services have been started!
echo.
echo   Opened windows:
echo   - iSipnayan Frontend (npm run dev)
echo   - iSipnayan Backend API (npm run dev)
echo   - iSipnayan Media Server (python app.py)
echo.
echo   To stop all services:
echo   1. Close the Frontend window
echo   2. Close the Backend API window
echo   3. Close the Media Server window
echo.
echo ================================================
pause
echo.

REM Ask if user wants to start frontend
set /p FRONTEND="Do you want to start the Frontend? y/n: "
if /i "%FRONTEND%"=="y" (
    echo.
    echo Starting Frontend Vite...
    cd /d "%FRONTEND_DIR%"
    if not exist "node_modules" (
        echo Installing dependencies...
        call npm install
    )
    echo.
    echo Starting on http://localhost:5173...
    start "iSipnayan Frontend" cmd /k "npm run dev"
) else (
    echo Frontend startup skipped.
)

echo.
echo All services are starting. Check the opened windows for status.
echo.
pause
