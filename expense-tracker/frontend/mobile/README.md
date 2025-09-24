# Expense Tracker

Full-stack expense tracking application with automated financial data extraction and analytics.

## 🏗️ Architecture

- **Backend**: Django REST Framework BFF
- **Frontend Web**: React with Redux Toolkit
- **Frontend Mobile**: React Native
- **Database**: PostgreSQL
- **Cache/Queue**: Redis + Celery
- **Integrations**: Plaid, Gmail, Twilio APIs

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 16+
- PostgreSQL 13+
- Redis 6+

### Backend Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Frontend Web Setup
```bash
cd frontend/web
npm install
npm start
```

### Frontend Mobile Setup
```bash
cd frontend/mobile
npm install
npx react-native run-android  # or run-ios
```

## 📱 Features

### Core Features
- ✅ Manual transaction entry
- ✅ Category management and auto-categorization
- ✅ Budget creation and tracking
- ✅ Subscription management
- ✅ Spending analytics and insights
- ✅ Multi-device synchronization

### Advanced Features
- 🏦 **Bank Integration**: Automatic transaction import via Plaid
- 📧 **Email Parsing**: Receipt extraction from Gmail
- 📱 **SMS Processing**: Bank notification parsing
- 📊 **Smart Analytics**: ML-powered spending insights
- 🔔 **Real-time Notifications**: Budget alerts and reminders
- 💳 **Multi-account Support**: Track multiple bank accounts
- 🌍 **Multi-currency**: Support for different currencies

## 🛠️ Development

### Project Structure
```
expense-tracker/
├── backend/              # Django BFF
│   ├── apps/            # Django apps (domain modules)
│   ├── core/            # Shared utilities
│   └── expense_tracker/ # Django project settings
├── frontend/
│   ├── web/             # React web application
│   └── mobile/          # React Native mobile app
├── docs/                # Documentation
└── scripts/             # Deployment scripts
```

### Key Technologies
- **Django 4.2**: Web framework with DRF
- **Celery**: Background task processing
- **React 18**: Frontend web framework
- **React Native 0.72**: Mobile development
- **Redux Toolkit**: State management
- **PostgreSQL**: Primary database
- **Redis**: Cache and message broker

### Integration APIs
- **Plaid**: Bank account connectivity
- **Gmail API**: Email receipt processing
- **Twilio**: SMS transaction parsing
- **OCR Services**: Receipt image processing

## 🔧 Development Tools

```bash
# Backend
make dev-backend          # Start Django server
make test-backend         # Run backend tests
make migrate             # Run database migrations

# Frontend
make dev-frontend-web    # Start React dev server
make dev-frontend-mobile # Start React Native

# Docker
make docker-up           # Start all services
make docker-down         # Stop all services

# Utilities
make format             # Format Python code
make lint              # Lint Python code
make clean            # Clean temporary files
```

## 🌟 BFF Architecture Benefits

The Backend-for-Frontend pattern provides:
- **Optimized APIs**: Tailored endpoints for web vs mobile clients
- **Data Aggregation**: Single API calls fetch data from multiple sources
- **Security**: Centralized authentication and authorization
- **Performance**: Caching and request optimization
- **Flexibility**: Easy to adapt for different client needs

## 📚 Documentation

- [API Documentation](docs/API.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [Architecture Overview](docs/ARCHITECTURE.md)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details
