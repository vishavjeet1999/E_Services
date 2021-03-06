# Generated by Django 4.0.3 on 2022-05-08 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=40)),
                ('service_charges', models.IntegerField()),
                ('service_description', models.CharField(max_length=500)),
                ('service_rating', models.IntegerField()),
                ('service_category', models.CharField(max_length=40)),
                ('service_long', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('service_lat', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
            ],
        ),
    ]
