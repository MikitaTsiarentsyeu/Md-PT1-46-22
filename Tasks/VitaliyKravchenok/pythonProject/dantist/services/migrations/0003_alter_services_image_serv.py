# Generated by Django 4.0.4 on 2022-06-05 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_services_image_serv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='image_serv',
            field=models.ImageField(upload_to='services/static/services/img'),
        ),
    ]