@echo off

call %~dp0\venv\Scripts\activate
cd %~dp0\pybot
set TOKEN=5655353500:AAHeMfLZ_cLwKJU8kPFjn9dn-y5loWAWZXw
set CHANNEL_ID=-1001762333718


python main.py

pause