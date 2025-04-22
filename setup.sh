#!/bin/bash
echo "Creating project structure..."
mkdir -p static/css
mkdir -p static/js
mkdir -p templates

echo "Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo "Setup complete! You can now run the application with ./run.sh"