# Generated by Django 3.2.7 on 2021-10-28 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artikel_page', '0014_alter_artikel_gambar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='gambar',
            field=models.ImageField(blank=True, default='static/image/default.jpg', upload_to='static/image/'),
        ),
    ]
