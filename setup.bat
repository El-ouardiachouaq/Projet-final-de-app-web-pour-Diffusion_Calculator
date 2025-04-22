@echo off
echo Creating project structure...
if not exist static\css mkdir static\css
if not exist static\js mkdir static\js
if not exist templates mkdir templates

echo Setting up virtual environment...
python -m venv venv
call venv\Scripts\activate.bat

echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

echo Setup complete! You can now run the application with run.bat
pause