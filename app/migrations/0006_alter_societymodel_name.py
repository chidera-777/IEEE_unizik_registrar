# Generated by Django 5.0.1 on 2024-02-08 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_societymodel_usersociety'),
    ]

    operations = [
        migrations.AlterField(
            model_name='societymodel',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
