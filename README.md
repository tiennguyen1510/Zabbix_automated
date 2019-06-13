# Zabbix Automation Tool

This is a tool for create multiple item and trigger. You have a template for key item and you can use this tool monitor the result. 

## 1. Diagram
![zabbix_automation](https://user-images.githubusercontent.com/34707129/59181958-b2a2a380-8b92-11e9-8735-44f64d847760.png)

## 2. Install

1. In computer client, you modiifies file list_file.txt with file you want.
2. Then, you run file python with command 
  ```bash
  python main.py
  ```
3. Then, you check items, triggers was created in Zabbix server,
4. In server zabbix agent, you run file zabbix_crontab and set crontab
  ```bash
  /bin/bash zabbix_crontab.sh
  ```
5. In Zabbix interface, you turn on trigger and check status
## 3. Related work
  - Read file csv [item, trigger, hostname,... ]
  - Split the file json.
  - Run follow arguments.
  - User and pass need to be encrypted.
  - Check key of items exist.
