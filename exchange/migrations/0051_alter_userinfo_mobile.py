# Generated by Django 3.2.6 on 2021-09-06 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0050_mobilecodes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='mobile',
            field=models.CharField(max_length=100),
        ),
    ]