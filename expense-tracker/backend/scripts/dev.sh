#!/bin/bash
# Development start script

echo "Starting development server..."

# Activate virtual environment
source venv/bin/activate

# Install/update dependencies
pip install -r requirements-dev.txt

# Run migrations
python manage.py migrate

# Create superuser if it doesn't exist
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser created: admin/admin123')
"

# Start development server
python manage.py runserver 0.0.0.0:8000
