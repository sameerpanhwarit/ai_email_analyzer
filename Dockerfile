FROM python:3.11-slim

WORKDIR /app

COPY . .

WORKDIR /app/AI_email_API

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run migrations and then start Gunicorn
CMD ["sh", "-c", "python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:8000"]
