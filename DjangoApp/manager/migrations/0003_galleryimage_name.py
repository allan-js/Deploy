# Generated by Django 4.1.7 on 2023-04-04 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_alter_staff_options_meal_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='name',
            field=models.CharField(default=0, help_text='Image name describes the image', max_length=75, verbose_name='Image Name'),
            preserve_default=False,
        ),
    ]