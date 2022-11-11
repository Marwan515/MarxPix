# Generated by Django 4.1.3 on 2022-11-08 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imagegen', '0002_remove_genimages_user_id_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cameras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cam', models.TextField()),
                ('cam_full', models.TextField()),
                ('rover_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imagegen.rovers')),
            ],
        ),
    ]