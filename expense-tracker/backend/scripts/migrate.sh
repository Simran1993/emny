#!/bin/bash
# Database migration script

echo "Running database migrations..."

# Activate virtual environment
source venv/bin/activate

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

echo "Migrations completed!"
