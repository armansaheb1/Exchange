# Generated by Django 3.2.6 on 2021-10-26 12:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0096_auto_20211022_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='verify',
            name='acceptv',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='buyoutrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 12, 23, 16, 971482, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='buyrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 12, 23, 16, 970464, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cp_withdraw',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 12, 23, 16, 977308, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='forgetrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 12, 23, 16, 984252, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='maintradesbuyorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 12, 23, 16, 987307, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='maintradessellorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 12, 23, 16, 987949, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 12, 23, 16, 985828, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='perpetualrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 12, 23, 16, 974177, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='protradesbuyorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 12, 23, 16, 988490, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='protradessellorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 12, 23, 16, 989019, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 12, 23, 16, 969149, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='selloutrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 12, 23, 16, 972957, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sellrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 12, 23, 16, 970986, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='smsverified',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 12, 23, 16, 968390, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 12, 23, 16, 982588, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 12, 23, 16, 983141, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 26, 12, 23, 16, 981425, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='verifyacceptrequest',
            name='acceptimg',
            field=models.ImageField(default='', upload_to='accept'),
            preserve_default=False,
        ),
    ]
