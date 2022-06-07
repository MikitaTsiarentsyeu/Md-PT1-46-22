# Generated by Django 4.0.4 on 2022-05-28 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='anonymous', max_length=30, verbose_name='Author')),
                ('date', models.DateTimeField(verbose_name='Publication date')),
                ('preview', models.CharField(max_length=200, verbose_name='Preview')),
                ('full_text', models.TextField(max_length=10000, verbose_name='Comment')),
            ],
        ),
    ]
