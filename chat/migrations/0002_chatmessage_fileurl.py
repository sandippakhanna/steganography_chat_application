# Generated by Django 4.0.1 on 2022-02-12 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='fileURL',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
