FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
COPY requirements /app/requirements
RUN pip install -r requirements.txt

COPY . /app/

# Load environment variables from .env file
ARG ENV_FILE
ENV ENV_FILE=${ENV_FILE:-.env.production}
COPY $ENV_FILE /app/.env

# Run migrations
RUN python manage.py migrate

# Expose the port the app will run on
EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "config.wsgi:application"]
