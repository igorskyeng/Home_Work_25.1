# Generated by Django 5.0.4 on 2024-05-24 05:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_options_alter_payments_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='payment_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 24, 13, 58, 31, 966642), verbose_name='Дата оплаты'),
        ),
    ]
