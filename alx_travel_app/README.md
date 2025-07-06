# ALX Travel App

A comprehensive Django-based travel listings platform with REST API, Swagger documentation, and Celery task queue integration.

## Features

- **Django REST Framework** - Full-featured REST API
- **Swagger Documentation** - Interactive API documentation at `/swagger/`
- **MySQL Database** - Production-ready database configuration
- **Celery Integration** - Asynchronous task processing
- **CORS Support** - Cross-origin resource sharing for frontend integration
- **Environment Variables** - Secure configuration management
- **Docker Ready** - Containerization support

## Quick Start

### Prerequisites

- Python 3.8+
- MySQL 8.0+
- Redis (for Celery)
- RabbitMQ (alternative message broker)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd alx_travel_app
   ```

2. **Create and activate virtual environment:**
   ```bash
   python3 -m venv backend_env
   source venv/bin/activate  # On Windows: backend_env\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

5. **Create MySQL database:**
   ```sql
   CREATE DATABASE alx_travel_db;
   CREATE USER 'your_db_user'@'localhost' IDENTIFIED BY 'your_db_password';
   GRANT ALL PRIVILEGES ON alx_travel_db.* TO 'your_db_user'@'localhost';
   FLUSH PRIVILEGES;
   ```

6. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

8. **Start development server:**
   ```bash
   python manage.py runserver
   ```

## API Documentation

- **Swagger UI:** http://localhost:8000/swagger/
- **ReDoc:** http://localhost:8000/redoc/
- **JSON Schema:** http://localhost:8000/swagger.json

## Project Structure

```
alx_travel_app/
├── alx_travel_app/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── celery.py
├── listings/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── static/
├── media/
├── templates/
├── .env
├── .gitignore
├── requirements.txt
└── manage.py
```

## Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# Database Configuration
DB_NAME=alx_travel_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306

# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Celery Configuration
CELERY_BROKER_URL=pyamqp://guest@localhost//
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

## Celery Setup

1. **Start Redis server:**
   ```bash
   redis-server
   ```

2. **Start Celery worker:**
   ```bash
   celery -A alx_travel_app worker --loglevel=info
   ```

3. **Start Celery beat (for periodic tasks):**
   ```bash
   celery -A alx_travel_app beat --loglevel=info
   ```

## Development

### Running Tests

```bash
python manage.py test
```

### Code Formatting

```bash
# Format code with black
black .

# Sort imports with isort
isort .

# Lint with flake8
flake8 .
```

### Database Operations

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic
```

## Deployment

### Production Settings

1. Set `DEBUG=False` in production
2. Configure proper `ALLOWED_HOSTS`
3. Use a production-grade database
4. Set up proper logging
5. Use a reverse proxy (nginx)
6. Configure SSL/TLS

### Docker Deployment

```dockerfile
# Dockerfile example
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please contact the development team or create an issue in the repository.

# AUTHOR
- Simanga Mchunu