# Generated by Django 5.0.4 on 2024-04-09 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_answer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='is_checkbox',
            field=models.BooleanField(default=False),
        ),
    ]