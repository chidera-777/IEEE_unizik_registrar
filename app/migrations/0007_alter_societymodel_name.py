# Generated by Django 5.0.1 on 2024-02-08 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_societymodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='societymodel',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
