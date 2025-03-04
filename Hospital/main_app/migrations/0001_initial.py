# Generated by Django 4.2.2 on 2023-06-09 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('feature_image', models.ImageField(default='images/default.jpg', upload_to='images/')),
                ('description', models.TextField()),
                ('department', models.CharField(choices=[('Heart Center', 'Heart Center'), ('euroscience Center', 'euroscience Center'), ('Obesity Center', 'Obesity Center'), ('Eye Center', 'Eye Center'), ('Orthopedic Center', 'Orthopedic Center'), ('Pediatric Center', 'Pediatric Center')], default='center', max_length=100)),
                ('established_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_description', models.TextField()),
                ('patient_age', models.IntegerField()),
                ('appointment_datetime', models.DateTimeField(auto_now_add=True)),
                ('is_attended', models.BooleanField(default=False)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.clinic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
