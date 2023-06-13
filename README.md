﻿# BID BUDDY

BID BUDDY Project is a web application that enables users to participate in auctions for various items. It provides features such as user registration and authentication, an auction gallery to browse available items, the ability to place bids on items. Also, Included some endpoints for the Admin dashboard and statistics that not includes in frontend yet

# Technology & Frameworks used

## BACKEND
* DJANGO
* DJANGO REST FRAMEWORK
* DJANGO Simple-JWT TOKEN
* JWT-Code for de-coding

# CHALLENGES
* As I used Django Simple JWT for Authentication, I forget to set LocalStorage and this loss my hours of work.
* I forget to set MEDIA URL and Static URL into root url, Instead I set to auction app url. this cause me some time.

# INSTALLATION

```bash
git clone https://github.com/hkshakib/auctionbackend.git
```
```bash
pip install -r requirements.txt
```
```bash
python manage.py makemigrations
python manage.py migrate
```
```bash
python manage.py runserver
```

# Limitation
* Due to time constraints, the project does not include an admin panel interface at the moment. The focus has been on developing user-facing features and core functionality related to auctions. While there is currently no dedicated section for administrators to manage the platform, future updates may incorporate an admin panel to provide advanced administrative capabilities.
