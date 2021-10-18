# Generated by Django 3.2.6 on 2021-10-17 13:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0082_auto_20211017_1348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='is_smsverified',
            new_name='smsverified',
        ),
        migrations.AlterField(
            model_name='buyrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 17, 13, 49, 47, 351388, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cp_withdraw',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 17, 13, 49, 47, 356732, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='forgetrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 17, 13, 49, 47, 363050, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='maintradesbuyorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 17, 13, 49, 47, 366077, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='maintradessellorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 17, 13, 49, 47, 366601, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 17, 13, 49, 47, 364504, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='perpetualrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 17, 13, 49, 47, 352807, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='protradesbuyorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 17, 13, 49, 47, 367129, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='protradessellorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 17, 13, 49, 47, 367654, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 17, 13, 49, 47, 350012, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sellrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 17, 13, 49, 47, 351878, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 17, 13, 49, 47, 361389, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 17, 13, 49, 47, 361940, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 17, 13, 49, 47, 360284, tzinfo=utc)),
        ),
    ]