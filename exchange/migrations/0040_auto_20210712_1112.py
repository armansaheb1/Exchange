# Generated by Django 3.2.3 on 2021-07-12 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exchange', '0039_auto_20210712_0735'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainTradesBuyOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('price', models.FloatField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('act', models.BooleanField()),
                ('trade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyorders', to='exchange.maintrades')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintradebuyorders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MainTradesSellOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('price', models.FloatField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('act', models.BooleanField()),
                ('trade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prosellorders', to='exchange.maintrades')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintradesellorders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProTradesBuyOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('price', models.FloatField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('act', models.BooleanField()),
                ('trade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='probuyorders', to='exchange.protrades')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='protradebuyorders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProTradesSellOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('price', models.FloatField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('act', models.BooleanField()),
                ('trade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prosellorders', to='exchange.protrades')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='protradesellorders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='protradesorder',
            name='maintrade',
        ),
        migrations.RemoveField(
            model_name='protradesorder',
            name='user',
        ),
        migrations.DeleteModel(
            name='MainTradesOrder',
        ),
        migrations.DeleteModel(
            name='ProTradesOrder',
        ),
    ]