# Generated by Django 3.2.7 on 2021-10-28 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artikel_page', '0016_alter_artikel_gambar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='deskripsi',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='artikel',
            name='judul',
            field=models.CharField(max_length=150),
        ),
    ]
