@echo off
title Touchless AI Reader

cd /d "%~dp0"

call venv\Scripts\activate

python src\app\touchless_reader_app.py

pause
