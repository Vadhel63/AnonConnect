# Generated by Django 4.2.10 on 2024-02-24 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_room_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='type',
            field=models.CharField(max_length=20),
        ),
    ]
