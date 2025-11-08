Interview API Project
Description

This project demonstrates interaction with the test API at https://test.icorp.uz/interview.php.
The goal is to fetch two parts of a code via POST and GET requests, combine them, and retrieve the final message.

Prerequisites

Python 3.13

Django 5.2

Django REST Framework

Docker + Docker Compose (optional)

requests library (for external HTTP requests)

Local Setup (Development)
1. Clone the repository
git clone <your-repo-url>
cd <your-project-folder>

2. Create a virtual environment
python -m venv venv

3. Activate the virtual environment

Linux/Mac

source venv/bin/activate


Windows

venv\Scripts\activate

4. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

5. Create .env file

Copy .env.example to .env and set your environment variables:

cp .env.example .env  # Linux/Mac
copy .env.example .env  # Windows


Edit .env to configure SECRET_KEY, DEBUG, ALLOWED_HOSTS, and database credentials.

6. Apply migrations
python manage.py makemigrations
python manage.py migrate

7. Create superuser (optional, for admin access)
python manage.py createsuperuser

8. Collect static files
python manage.py collectstatic --no-input

9. Run the server locally
python manage.py runserver


Default: http://127.0.0.1:8000

Using Docker (Local / Production)
1. Build and run containers
docker compose up -d


This will:

Start Django app

Start PostgreSQL container

Run migrations and collect static files (via entrypoint.sh / Makefile)

2. Stop containers
docker compose down

3. Optional Makefile commands

If you have a Makefile, you can run:

make install        # Install dependencies
make migrate        # Run migrations
make collectstatic  # Collect static files
make run            # Migrate + collectstatic + run server
make up             # docker compose up -d
make down           # docker compose down

Endpoints

POST /api/v1/api/get_second_part/ — Receive the second part of the code.

GET /api/v1/api/get_final_answer/ — Retrieve the concatenated code and final result.

Example Usage

Send a POST request to get_second_part/ with JSON:

{
  "part2": "<second part of the code>"
}


Send a GET request to get_final_answer/ to receive:

{
  "part1": "<first part>",
  "part2": "<second part>",
  "part1 + part2": "<combined code>",
  "result": "<final message>"
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

RESULT:
{
    "part1": "3b6050ea-a3d4-4fc8",
    "part2": "-86f4-bec75ca0b0c5",
    "part1 + part2": "3b6050ea-a3d4-4fc8-86f4-bec75ca0b0c5",
    "result": [
        "{\"msg\":\"Salom\"}"
    ]
}
