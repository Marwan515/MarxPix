# Generated by Django 4.1.3 on 2022-11-08 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagegen', '0003_cameras'),
    ]

    operations = [
        migrations.AddField(
            model_name='rovers',
            name='first_photos',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
