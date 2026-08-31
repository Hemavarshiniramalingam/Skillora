from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import StudentProfile


class StudentProfileTests(TestCase):
    def test_student_profile_can_be_created_for_user(self):
        user = get_user_model().objects.create_user(
            username='student1',
            email='student1@example.com',
            password='StrongPass123!'
        )

        profile = StudentProfile.objects.create(
            user=user,
            university='University of Nairobi',
            major='Computer Science',
            graduation_year=2027,
            gpa=4.2,
        )

        self.assertEqual(profile.user.username, 'student1')
        self.assertIn('Computer Science', str(profile))
