# Generated by Django 3.1.5 on 2021-01-13 10:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transactionOn', models.DateTimeField(default=datetime.datetime(2021, 1, 13, 10, 0, 48, 867107))),
                ('depositBy', models.TextField(max_length=300)),
                ('deposit', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('withdraw', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('accountNo', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accNo', models.PositiveIntegerField(unique=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('account_open', models.DateField(blank=True, null=True)),
                ('deposit', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('withdraw', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
