# Generated by Django 5.0.4 on 2024-05-21 07:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_payments_paid_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='payment_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 21, 15, 42, 59, 318532), verbose_name='Дата оплаты'),
        ),
    ]
