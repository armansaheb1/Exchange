# Generated by Django 3.2.3 on 2021-07-07 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0030_remove_verifymellirequest_verify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifybankrequest',
            name='bankc',
            field=models.BigIntegerField(null=True),
        ),
    ]