# FrogmiTest
This README provides comprehensive instructions for setting up and understanding the technical test provided by Frogmi. This was created with a Django Framework.

- ## Description
The technical test included two (2) important challenges, get "features" from a GeoJson and save it on a BD without duplicating it every time you had

#### Features
- Get data from a GeoJson
- Create a comment for a Feature
- Feed to see posts of other users<br>
- User details and button to update profile<br>
- Post detail view when clicking a post<br>

#### Technologies
- Python
- Django
- Sqlite

#### Folders Structure

```bash

├─ .gitignore
├─ .vscode
│  └─ launch.json
├─ docker-compose.yml
├─ dockerfile
├─ manage.py
├─ README.md
├─ requirements.txt
└─ sismic_api
   ├─ asgi.py
   ├─ settings.py
   ├─ sismic_data
   │  ├─ admin.py
   │  ├─ api.py
   │  ├─ apps.py
   │  ├─ migrations
   │  │  ├─ 0001_initial.py
   │  │  ├─ 0002_comment.py
   │  │  └─ __init__.py
   │  ├─ models
   │  │  ├─ comments.py
   │  │  ├─ features.py
   │  │  └─ __init__.py
   │  ├─ serializers
   │  │  ├─ comments.py
   │  │  ├─ features.py
   │  │  └─ __init__.py
   │  ├─ tests.py
   │  ├─ urls.py
   │  ├─ views
   │  │  ├─ comments.py
   │  │  ├─ features.py
   │  │  └─ __init__.py
   │  └─ __init__.py
   ├─ urls.py
   ├─ wsgi.py
   └─ __init__.py

```

- ## Installation

Fork the project and open Docker Desktop

Second, build the container
``` docker-compose build ```

Initialize the project:
``` docker-compose up ```
