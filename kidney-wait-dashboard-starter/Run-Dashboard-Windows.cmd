@echo off
cd /d "%~dp0"
py -m streamlit run dashboard/app.py
if errorlevel 1 echo If Streamlit is missing, run: py -m pip install -r requirements-dashboard.txt
pause
