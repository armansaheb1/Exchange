# Generated by Django 3.2.12 on 2022-05-17 15:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsverified',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 15, 6, 45, 804096)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='otp',
            field=models.CharField(default='vypjte8dfxvbbs45', max_length=100),
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin', models.CharField(max_length=100)),
                ('amount', models.FloatField(null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]