# Generated by Django 4.1.7 on 2023-04-04 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_galleryimage_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baseinfo',
            options={'verbose_name': 'Base Info', 'verbose_name_plural': 'Base Info'},
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(help_text='Upload you images to show up on the page front', upload_to='Images/Banners/%Y/%M/%d'),
        ),
    ]
