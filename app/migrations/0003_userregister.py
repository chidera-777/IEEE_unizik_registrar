# Generated by Django 5.0.1 on 2024-02-02 13:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_customuser_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('level', models.PositiveIntegerField(choices=[(100, 100), (200, 200), (300, 300), (400, 400), (500, 500)])),
                ('IEEE_number', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-email'],
            },
        ),
    ]