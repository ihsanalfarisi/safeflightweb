# Generated by Django 3.2.7 on 2021-10-27 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artikel_page', '0008_auto_20211028_0307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artikel',
            old_name='time_published',
            new_name='date_published',
        ),
    ]
