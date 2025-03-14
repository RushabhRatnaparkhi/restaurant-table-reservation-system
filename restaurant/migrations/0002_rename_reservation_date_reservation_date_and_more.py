# Generated by Django 5.1.7 on 2025-03-07 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='reservation_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='reservation_time',
            new_name='time',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='payment_status',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='transaction_id',
        ),
        migrations.RemoveField(
            model_name='table',
            name='capacity',
        ),
        migrations.RemoveField(
            model_name='table',
            name='status',
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(default='Cash', max_length=50),
        ),
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')], default='Pending', max_length=20),
        ),
        migrations.AddField(
            model_name='table',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='table',
            name='seats',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='table',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurant.table'),
        ),
    ]
