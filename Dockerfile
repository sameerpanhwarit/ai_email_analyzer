FROM python:3.11-slim

WORKDIR /app

COPY . .

WORKDIR /app/AI_email_Analyzer

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run Gunicorn from inside the project subdirectory
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
