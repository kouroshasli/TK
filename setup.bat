@echo off
echo Setting up Kouroshasli Website...

REM Create virtual environment if it doesn't exist
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install required packages
echo Installing required packages...
pip install -r requirements.txt

echo Setup completed!
echo You can now run run.bat to start the website.
pause 