# Generated by Django 3.2.6 on 2021-08-10 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0049_auto_20210802_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='mobilecodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15)),
                ('code', models.CharField(max_length=15)),
            ],
        ),
    ]
