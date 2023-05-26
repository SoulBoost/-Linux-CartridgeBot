# -Linux-CartridgeBot
TelegramBot с картриджем, который нонстопом работает на линуксе.



systemd:                                                                                                                       
 [Unit]
 # описание
 Description=pythonbot
 # здесь используется ключи времени с указанием цели или другой службы
 After=prefdm.service

 [Service]
 # от какого пользователя запускать службу, не обязательно
 User=root
 # перезапуск службы, не обязательно
 #Restart=on-failure
 #выполняемая команда
# ExecStart=bash /home/vignatenko/pybot/pybot/PythonBot.sh
WorkingDirectory=/home/vignatenko/pybot/pybot
ExecStart = python /home/vignatenko/pybot/pybot/main.py
#Restart = Always

 [Install]
 # здесь используется ключи времени с указанием цели или другой службы
# WantedBy=network.target
WantedBy=multi-user.target
