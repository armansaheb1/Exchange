# Generated by Django 3.2.3 on 2021-07-10 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0035_notification_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainTrades',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name=' نام ارز')),
                ('brand', models.CharField(max_length=100, null=True, verbose_name=' نماد ارز')),
            ],
        ),
        migrations.CreateModel(
            name='ProTrades',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name=' نام ارز')),
                ('brand', models.CharField(max_length=100, null=True, verbose_name=' نماد ارز')),
            ],
        ),
    ]