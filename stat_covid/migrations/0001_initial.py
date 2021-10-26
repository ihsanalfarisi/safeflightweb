# Generated by Django 3.2.8 on 2021-10-26 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=50)),
                ('code', models.CharField(editable=False, max_length=3)),
            ],
        ),
    ]
