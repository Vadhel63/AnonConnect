# Generated by Django 4.2.10 on 2024-02-25 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_remove_room_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='password',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]