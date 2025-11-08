Interview API Project

This project demonstrates interaction with the test API at https://test.icorp.uz/interview.php
.
The goal is to fetch two parts of a code via POST and GET requests, combine them, and retrieve the final message.

Prerequisites

Python 3.13

Django 5.2

Django REST Framework

Docker + Docker Compose (optional)

requests library (for external HTTP requests)

Local Setup (Development)

Clone the repository

git clone <repository_url>
cd <repository_folder>


Create a virtual environment

python -m venv venv


Activate the virtual environment

Linux/Mac

source venv/bin/activate


Windows

venv\Scripts\activate


Install dependencies

pip install --upgrade pip
pip install -r requirements.txt


Create .env file

# Linux/Mac
cp .env.example .env

# Windows
copy .env.example .env


Edit .env to configure:

SECRET_KEY

DEBUG

ALLOWED_HOSTS

Database credentials

Apply migrations

python manage.py makemigrations
python manage.py migrate


Create superuser (optional, for admin access)

python manage.py createsuperuser


Collect static files

python manage.py collectstatic --no-input


Run the server locally

python manage.py runserver


Default URL: http://127.0.0.1:8000

Using Docker (Local / Production)

Build and run containers

docker compose up -d


This will:

Start Django app

Start PostgreSQL container

Run migrations and collect static files (via entrypoint.sh / Makefile)

Stop containers

docker compose down

Optional Makefile Commands
make install        # Install dependencies
make migrate        # Run migrations
make collectstatic  # Collect static files
make run            # Migrate + collectstatic + run server
make up             # docker compose up -d
make down           # docker compose down

API Endpoints

POST /api/v1/api/get_second_part/ — Receive the second part of the code.

GET /api/v1/api/get_final_answer/ — Retrieve the concatenated code and final result.

Example Usage

Send a POST request to get_second_part/ with JSON:

{
  "part2": ""
}


Send a GET request to get_final_answer/ to receive:

{
  "part1": "",
  "part2": "",
  "part1 + part2": "",
  "result": ""
}


Sample Result:

{
  "part1": "3b6050ea-a3d4-4fc8",
  "part2": "-86f4-bec75ca0b0c5",
  "part1 + part2": "3b6050ea-a3d4-4fc8-86f4-bec75ca0b0c5",
  "result": [
    {"msg": "Salom"}
  ]
}

Project Structure
.
├── api/                 # App with API logic
├── config/              # Django settings
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── Makefile
├── requirements.txt
└── README.md
