# Generated by Django 4.2.3 on 2023-07-26 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagedetection', '0002_rename_file_serial_detection_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serial_detection',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
