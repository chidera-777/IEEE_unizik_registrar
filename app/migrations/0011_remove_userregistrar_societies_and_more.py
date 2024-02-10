# Generated by Django 5.0.1 on 2024-02-09 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_societymodel_user_userregistrar_societies_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userregistrar',
            name='societies',
        ),
        migrations.AddField(
            model_name='userregistrar',
            name='societies',
            field=models.ManyToManyField(blank=True, related_name='societies_joined', to='app.societymodel'),
        ),
    ]
