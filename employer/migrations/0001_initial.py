# Generated by Django 4.0.4 on 2022-05-20 16:03

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
            name='EmployerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=120, unique=True)),
                ('logo', models.ImageField(upload_to='images')),
                ('bio', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=120)),
                ('services', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
