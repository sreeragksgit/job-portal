# Generated by Django 4.0.4 on 2022-05-25 05:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employer', '0003_applications'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='applications',
            unique_together={('applicant', 'job')},
        ),
    ]
