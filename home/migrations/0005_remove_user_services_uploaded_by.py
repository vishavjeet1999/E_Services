# Generated by Django 4.0.3 on 2022-05-26 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_user_services_uploaded_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_services',
            name='uploaded_by',
        ),
    ]
