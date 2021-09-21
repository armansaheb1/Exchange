# Generated by Django 3.2.6 on 2021-09-20 16:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0069_auto_20210920_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cp_withdraw',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 20, 16, 21, 55, 834191, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='forgetrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 20, 16, 21, 55, 840657, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='maintradesbuyorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 20, 16, 21, 55, 843687, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='maintradessellorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 20, 16, 21, 55, 844211, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 20, 16, 21, 55, 842170, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='perpetual',
            name='apikey',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='perpetual',
            name='secretkey',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='perpetualrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 20, 16, 21, 55, 830004, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='protradesbuyorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 20, 16, 21, 55, 844729, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='protradessellorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 20, 16, 21, 55, 845314, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 20, 16, 21, 55, 839067, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 20, 16, 21, 55, 839678, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 20, 16, 21, 55, 838009, tzinfo=utc)),
        ),
    ]
