# Generated by Django 3.2.8 on 2021-10-29 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Regulasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('negara', models.CharField(default=None, max_length=30)),
            ],
        ),
    ]
