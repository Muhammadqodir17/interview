# Interview API Project

A Django REST Framework project that demonstrates interaction with an external test API to fetch, combine, and process code fragments.

## 📋 Overview

This project fetches two parts of code via POST and GET requests from `https://test.icorp.uz/interview.php`, combines them, and retrieves the final message.

---

## ✅ Prerequisites

- Python 3.13
- Django 5.2
- Django REST Framework
- Docker + Docker Compose (optional)
- `requests` library (for external HTTP requests)

---

## 🚀 Local Setup (Development)

### 1. Clone the Repository

\`\`\`bash
git clone <repository_url>
cd <repository_folder>
\`\`\`

### 2. Create a Virtual Environment

\`\`\`bash
python -m venv venv
\`\`\`

### 3. Activate the Virtual Environment

**Linux/Mac:**
\`\`\`bash
source venv/bin/activate
\`\`\`

**Windows:**
\`\`\`bash
venv\Scripts\activate
\`\`\`

### 4. Install Dependencies

\`\`\`bash
pip install --upgrade pip
pip install -r requirements.txt
\`\`\`

### 5. Configure Environment Variables

**Linux/Mac:**
\`\`\`bash
cp .env.example .env
\`\`\`

**Windows:**
\`\`\`bash
copy .env.example .env
\`\`\`

Edit `.env` to set:
- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- Database credentials

### 6. Run Migrations

\`\`\`bash
python manage.py makemigrations
python manage.py migrate
\`\`\`

### 7. Create Superuser (Optional)

\`\`\`bash
python manage.py createsuperuser
\`\`\`

### 8. Collect Static Files

\`\`\`bash
python manage.py collectstatic --no-input
\`\`\`

### 9. Start the Development Server

\`\`\`bash
python manage.py runserver
\`\`\`

Default URL: `http://127.0.0.1:8000`

---

## 🐳 Using Docker

### Build and Run Containers

\`\`\`bash
docker compose up -d
\`\`\`

This will:
- Start the Django application
- Start PostgreSQL container
- Run migrations and collect static files (via `entrypoint.sh` / `Makefile`)

### Stop Containers

\`\`\`bash
docker compose down
\`\`\`

---

## 🛠️ Makefile Commands

| Command | Description |
|---------|-------------|
| `make install` | Install dependencies |
| `make migrate` | Run migrations |
| `make collectstatic` | Collect static files |
| `make run` | Migrate + collectstatic + run server |
| `make up` | Docker compose up |
| `make down` | Docker compose down |

---

## 📡 API Endpoints

### POST `/api/v1/api/get_second_part/`
Receive the second part of the code.

**Request Example:**
\`\`\`json
{
  "part2": ""
}
\`\`\`

### GET `/api/v1/api/get_final_answer/`
Retrieve the concatenated code and final result.

**Response Example:**
\`\`\`json
{
  "part1": "3b6050ea-a3d4-4fc8",
  "part2": "-86f4-bec75ca0b0c5",
  "part1 + part2": "3b6050ea-a3d4-4fc8-86f4-bec75ca0b0c5",
  "result": [
    {
      "msg": "Salom"
    }
  ]
}
\`\`\`

---

## 📁 Project Structure

\`\`\`
.
├── api/                 # App with API logic
├── config/              # Django settings
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose setup
├── entrypoint.sh        # Container entrypoint script
├── Makefile             # Build automation
├── requirements.txt     # Python dependencies
└── README.md            # This file
\`\`\`

---

## 📝 License

Add your license information here.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.
