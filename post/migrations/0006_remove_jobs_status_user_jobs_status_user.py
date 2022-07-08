# Generated by Django 4.0.6 on 2022-07-08 07:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0005_jobs_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs_status',
            name='user',
        ),
        migrations.AddField(
            model_name='jobs_status',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
