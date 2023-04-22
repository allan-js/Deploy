# Generated by Django 4.1.7 on 2023-04-18 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_rename_about_meal_description_meal_price'),
        ('booking', '0004_alter_booking_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='manager.room'),
        ),
    ]