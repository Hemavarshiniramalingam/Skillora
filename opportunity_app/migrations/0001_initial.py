# Generated migration for opportunity_app models

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('major', models.CharField(blank=True, max_length=255)),
                ('gpa', models.FloatField(default=0.0)),
                ('preferred_fields', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('deadline', models.DateField()),
                ('skills_required', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('provider', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('deadline', models.DateField()),
                ('eligibility', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MatchResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opportunity_type', models.CharField(choices=[('internship', 'Internship'), ('scholarship', 'Scholarship')], max_length=20)),
                ('opportunity_id', models.IntegerField()),
                ('score', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_results', to='opportunity_app.student')),
            ],
            options={
                'ordering': ['-score', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='applied', max_length=50)),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('internship', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='opportunity_app.internship')),
                ('scholarship', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='opportunity_app.scholarship')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='opportunity_app.student')),
            ],
        ),
    ]
