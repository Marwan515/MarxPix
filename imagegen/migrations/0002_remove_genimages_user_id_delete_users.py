# Generated by Django 4.1.3 on 2022-11-03 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagegen', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genimages',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
