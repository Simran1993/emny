# Expense Tracker Django BFF Makefile

.PHONY: help setup install-backend install-frontend dev-backend dev-frontend dev test clean

help:  ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-15s\033[0m %s\n", $1, $2}' $(MAKEFILE_LIST)

setup: install-backend install-frontend  ## Setup the entire project

install-backend:  ## Install backend dependencies
	cd backend && python3 -m venv venv && source venv/bin/activate && pip install -r requirements-dev.txt

install-frontend:  ## Install frontend dependencies
	cd frontend/web && npm install
	cd frontend/mobile && npm install

dev-backend:  ## Start Django development server
	cd backend && source venv/bin/activate && python manage.py runserver

dev-frontend-web:  ## Start React web development server
	cd frontend/web && npm start

dev-frontend-mobile:  ## Start React Native development
	cd frontend/mobile && npx react-native start

dev:  ## Start all development servers
	make dev-backend & make dev-frontend-web &

test-backend:  ## Run backend tests
	cd backend && source venv/bin/activate && python manage.py test

test-frontend:  ## Run frontend tests
	cd frontend/web && npm test

test: test-backend test-frontend  ## Run all tests

migrate:  ## Run Django migrations
	cd backend && source venv/bin/activate && python manage.py migrate

makemigrations:  ## Create Django migrations
	cd backend && source venv/bin/activate && python manage.py makemigrations

superuser:  ## Create Django superuser
	cd backend && source venv/bin/activate && python manage.py createsuperuser

shell:  ## Open Django shell
	cd backend && source venv/bin/activate && python manage.py shell

clean:  ## Clean up temporary files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf backend/staticfiles/
	rm -rf frontend/web/build/
	rm -rf frontend/mobile/android/app/build/

docker-up:  ## Start Docker containers
	cd backend && docker-compose up -d

docker-down:  ## Stop Docker containers
	cd backend && docker-compose down

docker-logs:  ## View Docker logs
	cd backend && docker-compose logs -f

format:  ## Format Python code
	cd backend && source venv/bin/activate && black . && isort .

lint:  ## Lint Python code
	cd backend && source venv/bin/activate && flake8 .
