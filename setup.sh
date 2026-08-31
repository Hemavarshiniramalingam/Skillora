#!/bin/bash
# Quick start script for OpportunityAI development

set -e

echo "=========================================="
echo "OpportunityAI - Development Setup"
echo "=========================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Step 1: Install dependencies
echo -e "${BLUE}[1/5]${NC} Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
echo -e "${GREEN}✓ Dependencies installed${NC}"
echo ""

# Step 2: Setup environment
echo -e "${BLUE}[2/5]${NC} Setting up environment..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo -e "${GREEN}✓ Created .env file (edit as needed)${NC}"
else
    echo -e "${GREEN}✓ .env file already exists${NC}"
fi
echo ""

# Step 3: Run migrations
echo -e "${BLUE}[3/5]${NC} Running database migrations..."
python manage.py migrate
echo -e "${GREEN}✓ Migrations completed${NC}"
echo ""

# Step 4: Create superuser (optional)
echo -e "${BLUE}[4/5]${NC} Creating superuser..."
python manage.py createsuperuser --noinput --username=admin --email=admin@skillora.local || echo "Superuser may already exist"
echo ""

# Step 5: Validation
echo -e "${BLUE}[5/5]${NC} Validating setup..."
python validate_setup.py
echo ""

echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "To start development:"
echo ""
echo "Terminal 1 (Django dev server):"
echo "  python manage.py runserver"
echo ""
echo "Terminal 2 (Celery worker):"
echo "  celery -A skillora worker -l info"
echo ""
echo "Terminal 3 (Celery Beat):"
echo "  celery -A skillora beat -l info"
echo ""
echo "Then visit: http://localhost:8000/api/health/"
echo ""
