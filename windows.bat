
@echo off
REM ============================
REM Running Teaching Tool Web Server on Windows with Docker
REM ============================

REM ---- CONFIG ----
set IMAGE_NAME=com3524

REM ---- BUILD IMAGE ----
echo Building Docker image...
docker build -t %IMAGE_NAME% .

<<<<<<< HEAD
REM ---- RUN CONTAINER WITH INTERACTIVE SHELL----
=======
REM ---- RUN CONTAINER WITH INTERACTIVE SHELL ----
>>>>>>> 568fe0eba548eb8ec7dbba466c1aecbf9304d960
echo Running web app on http://127.0.0.1:5000 ...
docker run -it ^
    -e DISPLAY=host.docker.internal:0.0 ^
    -p 5000:5000 ^                 
    %IMAGE_NAME% ^
    bash

pause
