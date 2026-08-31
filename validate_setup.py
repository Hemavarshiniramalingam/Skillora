#!/usr/bin/env python
"""
Validation script to verify the OpportunityAI Django project setup.
Run this to ensure all components are properly configured.
"""

import os
import sys
import django
from pathlib import Path

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skillora.settings.dev")
django.setup()

from django.core.management import call_command
from django.db import connections
from django.apps import apps
import redis


def test_django_check():
    """Run Django system checks."""
    print("✓ Running Django system checks...")
    try:
        from django.core.management import execute_from_command_line
        from io import StringIO
        import sys
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        from django.core.management.color import no_style
        from django.core.management import call_command
        call_command('check', stdout=StringIO(), no_color=True)
        
        sys.stdout = old_stdout
        print("  ✓ All Django checks passed")
        return True
    except Exception as e:
        print(f"  ✗ Django check failed: {e}")
        return False


def test_database():
    """Test database connection."""
    print("✓ Testing database connection...")
    try:
        connection = connections['default']
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')
        print("  ✓ Database connection successful")
        return True
    except Exception as e:
        print(f"  ✗ Database connection failed: {e}")
        return False


def test_models():
    """Test that all models can be imported."""
    print("✓ Testing models...")
    try:
        from opportunity_app.models import (
            Student, Internship, Scholarship, Application, MatchResult
        )
        print(f"  ✓ Found {len([Student, Internship, Scholarship, Application, MatchResult])} models")
        return True
    except Exception as e:
        print(f"  ✗ Model import failed: {e}")
        return False


def test_serializers():
    """Test that all serializers can be imported."""
    print("✓ Testing serializers...")
    try:
        from opportunity_app.serializers import (
            StudentSerializer, InternshipSerializer, ScholarshipSerializer,
            ApplicationSerializer, MatchResultSerializer
        )
        print(f"  ✓ All serializers imported successfully")
        return True
    except Exception as e:
        print(f"  ✗ Serializer import failed: {e}")
        return False


def test_views():
    """Test that all views can be imported."""
    print("✓ Testing views...")
    try:
        from opportunity_app.views import (
            internship_list_create, scholarship_list_create,
            application_list_create, match_for_student, healthcheck
        )
        print(f"  ✓ All views imported successfully")
        return True
    except Exception as e:
        print(f"  ✗ View import failed: {e}")
        return False


def test_tasks():
    """Test that Celery tasks can be imported."""
    print("✓ Testing Celery tasks...")
    try:
        from opportunity_app.tasks import (
            send_deadline_reminders, send_new_opportunity_notification
        )
        print(f"  ✓ All Celery tasks imported successfully")
        return True
    except Exception as e:
        print(f"  ✗ Task import failed: {e}")
        return False


def test_celery():
    """Test Celery app configuration."""
    print("✓ Testing Celery configuration...")
    try:
        from skillora.celery import app as celery_app
        print(f"  ✓ Celery app configured: {celery_app.main}")
        return True
    except Exception as e:
        print(f"  ✗ Celery configuration failed: {e}")
        return False


def test_redis():
    """Test Redis connection (if configured)."""
    print("✓ Testing Redis connection...")
    try:
        from django.conf import settings
        broker_url = settings.CELERY_BROKER_URL
        
        if 'redis' in broker_url:
            # Parse Redis URL (format: redis://host:port/db)
            parts = broker_url.replace('redis://', '').split(':')
            host = parts[0]
            port = int(parts[1].split('/')[0]) if len(parts) > 1 else 6379
            db = int(parts[1].split('/')[-1]) if '/' in parts[1] else 0
            
            r = redis.Redis(host=host, port=port, db=db, decode_responses=True)
            r.ping()
            print(f"  ✓ Redis connection successful (redis://{host}:{port}/{db})")
            return True
        else:
            print(f"  ⚠ Redis not configured (broker: {broker_url})")
            return True
    except Exception as e:
        print(f"  ⚠ Redis connection failed: {e} (OK for development with console broker)")
        return True


def test_migrations():
    """Check if migrations are ready."""
    print("✓ Checking migrations...")
    try:
        from django.db.migrations.executor import MigrationExecutor
        from django.db import connections
        
        connection = connections['default']
        executor = MigrationExecutor(connection)
        
        plan = executor.migration_plan(executor.loader.graph.leaf_nodes())
        if plan:
            print(f"  ⚠ {len(plan)} migrations pending - run 'python manage.py migrate'")
        else:
            print(f"  ✓ All migrations applied")
        return True
    except Exception as e:
        print(f"  ✗ Migration check failed: {e}")
        return False


def test_apps():
    """Check installed apps."""
    print("✓ Checking installed apps...")
    try:
        installed = [app.name for app in apps.get_app_configs()]
        required = ['django.contrib.admin', 'rest_framework', 'opportunity_app']
        
        for app in required:
            if app not in installed:
                print(f"  ✗ Missing app: {app}")
                return False
        
        print(f"  ✓ All required apps installed ({len(required)} verified)")
        return True
    except Exception as e:
        print(f"  ✗ App check failed: {e}")
        return False


def test_settings():
    """Verify settings are loaded correctly."""
    print("✓ Checking settings...")
    try:
        from django.conf import settings
        
        required_settings = [
            'SECRET_KEY', 'DEBUG', 'ALLOWED_HOSTS', 'DATABASES',
            'INSTALLED_APPS', 'REST_FRAMEWORK', 'CELERY_BROKER_URL'
        ]
        
        missing = []
        for setting in required_settings:
            if not hasattr(settings, setting):
                missing.append(setting)
        
        if missing:
            print(f"  ✗ Missing settings: {', '.join(missing)}")
            return False
        
        print(f"  ✓ Settings loaded correctly")
        print(f"    - DEBUG: {settings.DEBUG}")
        print(f"    - ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
        print(f"    - Database: {settings.DATABASES['default']['ENGINE'].split('.')[-1]}")
        return True
    except Exception as e:
        print(f"  ✗ Settings check failed: {e}")
        return False


def main():
    """Run all validation tests."""
    print("=" * 60)
    print("OpportunityAI - Django Project Validation")
    print("=" * 60)
    print()
    
    tests = [
        ("Settings", test_settings),
        ("Django Checks", test_django_check),
        ("Apps", test_apps),
        ("Database", test_database),
        ("Models", test_models),
        ("Serializers", test_serializers),
        ("Views", test_views),
        ("Tasks", test_tasks),
        ("Celery", test_celery),
        ("Redis", test_redis),
        ("Migrations", test_migrations),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"✗ Test failed with exception: {e}")
            results.append((name, False))
        print()
    
    # Summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {name}")
    
    print()
    print(f"Total: {passed}/{total} checks passed")
    
    if passed == total:
        print("\n✓ All validation checks passed!")
        print("\nNext steps:")
        print("1. Run migrations: python manage.py migrate")
        print("2. Start dev server: python manage.py runserver")
        print("3. Start Celery: celery -A skillora worker -l info")
        print("4. Visit: http://localhost:8000/api/health/")
        return 0
    else:
        print(f"\n✗ {total - passed} check(s) failed. Please review errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
