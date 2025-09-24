#!/bin/bash
# Production start script

echo "Starting Expense Tracker Django BFF..."

# Activate virtual environment
source venv/bin/activate

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start gunicorn
gunicorn --bind 0.0.0.0:8000 expense_tracker.wsgi:application
