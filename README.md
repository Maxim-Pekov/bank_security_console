# BANK SECURITY CONSOLE

The bank security console is designed to detect and control passes to enter the bank vault.
There are several options:

___View all active passes___

___Display all visits of a specific pass___

___Show all passes in storage___



![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

---
## Installation
Use these commands to start a project on your hardware.
- [x] You can mark completed tasks with checkboxes 
1. Install

- [ ]    `git clone https://github.com/Maxim-Pekov/bank_security_console`

- [ ]    `python -m venv venv`
2. Activate venv    
- [ ] Windows  `.\venv\Scripts\activate`
- [ ] Linux, Mac  `source ./venv/bin/activate`
3. Go to the `./bank_security_console` directory
4. Install requirements

- [ ]    `pip install -r requirements.txt`

5. Create new file in main directory `.env`, where you will write your DATABASE_URL, DEBUG
- Replace the variables `( postgres, USER, PASSWORD, HOST, PORT, NAME )` with your own.
- [ ]    `DATABASE_URL = postgres://USER:PASSWORD@HOST:PORT/NAME`
    

- Your app raises an exception when DEBUG is True `True`.

- [ ]    `DEBUG = False`

6. Run this command

- [ ]   `python manage.py runserver`
---

## Changes _extra time_ to find strange user
```bash
1). Open ./datacenter/models.py
2). Find function find_long_visit()
3). Change 'strange_time_minutes' to your time by minutes
```

## Project Goals
Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.

## About me



[//]: # (Карточка профиля: )
![](https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Maxim-Pekov&theme=solarized_dark)

[//]: # (Статистика языков в коммитах:)
[//]: # (Статистика языков в репозиториях:)
![](https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=Maxim-Pekov&theme=solarized_dark)
![](https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=Maxim-Pekov&theme=solarized_dark)



[//]: # (Статистика профиля:)
[//]: # (Данные по коммитам за сутки:)
![](https://github-profile-summary-cards.vercel.app/api/cards/stats?username=Maxim-Pekov&theme=solarized_dark)
![](https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=Maxim-Pekov&theme=solarized_dark)

[//]: # ([![trophy]&#40;https://github-profile-trophy.vercel.app/?username=Maxim-Pekov&#41;]&#40;https://github.com/ryo-ma/github-profile-trophy&#41;)