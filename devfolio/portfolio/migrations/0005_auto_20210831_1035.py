# Generated by Django 3.1.13 on 2021-08-31 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20210831_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='live_url_message_modal_text',
            field=models.TextField(blank=True, max_length=300, verbose_name='Live URL Popup Message'),
        ),
    ]
