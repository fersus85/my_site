# Generated by Django 3.2.9 on 2023-05-15 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
