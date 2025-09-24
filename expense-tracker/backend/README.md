# Expense Tracker Django BFF

Backend-for-Frontend (BFF) service built with Django REST Framework for the Expense Tracker application.

## Features

- 🏦 **Financial Integrations**: Plaid API for bank account connectivity
- 📧 **Email Processing**: Gmail API for receipt parsing
- 📱 **SMS Integration**: Twilio for transaction SMS parsing
- 📊 **Analytics Engine**: Advanced spending analytics and budgeting
- 🔄 **Background Processing**: Celery for async task handling
- 🔐 **Authentication**: JWT-based secure authentication
- 📱 **Cross-platform APIs**: Optimized endpoints for web and mobile clients

## Quick Start

1. **Setup virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r requirements-dev.txt
```

3. **Setup database:**
```bash
python manage.py migrate
python manage.py createsuperuser
```

4. **Start development server:**
```bash
python manage.py runserver
```

5. **Start Celery worker (in another terminal):**
```bash
celery -A expense_tracker worker -l info
```

## API Documentation

- **Admin Panel**: http://localhost:8000/admin/
- **API Endpoints**: http://localhost:8000/api/
- **Health Check**: http://localhost:8000/api/health/

## Architecture

```
Django BFF
├── Apps (Domain-driven modules)
│   ├── authentication/     # JWT auth, user registration
│   ├── users/             # User management
│   ├── transactions/      # Transaction CRUD
│   ├── categories/        # Expense categorization
│   ├── budgets/          # Budget tracking
│   ├── subscriptions/    # Subscription management
│   ├── analytics/        # Spending analytics
│   └── integrations/     # External service integrations
├── Core (Shared utilities)
│   ├── authentication/   # Custom auth backends
│   ├── exceptions/       # Error handling
│   ├── middleware/       # Custom middleware
│   ├── services/         # Business logic
│   └── utils/           # Helper functions
└── External Integrations
    ├── Plaid API        # Bank connectivity
    ├── Gmail API        # Email receipt parsing
    ├── Twilio API       # SMS processing
    └── OCR Services     # Receipt image processing
```

## Environment Variables

Copy `.env.example` to `.env.local` and configure:

```env
SECRET_KEY=your-secret-key
DB_NAME=expense_tracker
DB_USER=postgres
DB_PASSWORD=password
PLAID_CLIENT_ID=your-plaid-client-id
PLAID_SECRET=your-plaid-secret
# ... see .env.example for full list
```

## Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test apps.transactions

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

## Deployment

### Docker

```bash
docker-compose up -d
```

### Production

```bash
# Collect static files
python manage.py collectstatic

# Run with Gunicorn
gunicorn --bind 0.0.0.0:8000 expense_tracker.wsgi:application
```
