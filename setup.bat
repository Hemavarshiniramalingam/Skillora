@echo off
REM Quick start script for OpportunityAI development (Windows)

setlocal enabledelayedexpansion

echo ==========================================
echo OpportunityAI - Development Setup
echo ==========================================
echo.

REM Step 1: Install dependencies
echo [1/5] Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt
echo [OK] Dependencies installed
echo.

REM Step 2: Setup environment
echo [2/5] Setting up environment...
if not exist .env (
    copy .env.example .env
    echo [OK] Created .env file (edit as needed)
) else (
    echo [OK] .env file already exists
)
echo.

REM Step 3: Run migrations
echo [3/5] Running database migrations...
python manage.py migrate
echo [OK] Migrations completed
echo.

REM Step 4: Create superuser (optional)
echo [4/5] Creating superuser...
python manage.py createsuperuser --noinput --username=admin --email=admin@skillora.local 2>nul || echo [INFO] Superuser may already exist
echo.

REM Step 5: Validation
echo [5/5] Validating setup...
python validate_setup.py
echo.

echo ==========================================
echo Setup Complete!
echo ==========================================
echo.
echo To start development:
echo.
echo Terminal 1 ^(Django dev server^):
echo   python manage.py runserver
echo.
echo Terminal 2 ^(Celery worker^):
echo   celery -A skillora worker -l info
echo.
echo Terminal 3 ^(Celery Beat^):
echo   celery -A skillora beat -l info
echo.
echo Then visit: http://localhost:8000/api/health/
echo.

pause
