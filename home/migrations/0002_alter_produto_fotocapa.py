# Generated by Django 4.1.1 on 2022-09-15 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='fotoCapa',
            field=models.ImageField(height_field=400, upload_to='media/% Y/% m/% d/', width_field=640),
        ),
    ]
