@echo off
echo Starting Kouroshasli Website...

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Run the development server
python manage.py runserver

REM Deactivate virtual environment when server is stopped
deactivate

pause 