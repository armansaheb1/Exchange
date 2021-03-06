# Generated by Django 3.2.12 on 2022-05-31 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatsessionmessage',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='chatsession',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='chatsession',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
