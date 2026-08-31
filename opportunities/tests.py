from django.test import TestCase

from .models import Application, Internship, Organization, Scholarship


class OpportunityModelsTests(TestCase):
    def test_organization_and_opportunity_models_create(self):
        org = Organization.objects.create(
            name='Skillora Labs',
            industry='EdTech',
            website='https://skillora.example',
        )

        internship = Internship.objects.create(
            organization=org,
            title='Backend Intern',
            location='Remote',
            internship_type='Remote',
            pay='Paid',
            deadline='2026-12-31',
        )

        scholarship = Scholarship.objects.create(
            organization=org,
            title='Women in Tech Scholarship',
            amount='USD 2000',
            deadline='2026-11-30',
        )

        application = Application.objects.create(
            internship=internship,
            status='submitted',
        )

        self.assertEqual(str(org), 'Skillora Labs')
        self.assertEqual(str(internship), 'Backend Intern')
        self.assertEqual(str(scholarship), 'Women in Tech Scholarship')
        self.assertEqual(str(application), 'submitted')
