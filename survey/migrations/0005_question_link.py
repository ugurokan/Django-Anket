# Generated by Django 5.0.4 on 2024-04-13 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_rename_is_checkbox_option_dogru_cevap'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='link',
            field=models.CharField(default='wwww.kaanenesciftci.com', max_length=2048),
            preserve_default=False,
        ),
    ]