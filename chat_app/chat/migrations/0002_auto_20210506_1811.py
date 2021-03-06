# Generated by Django 3.1.7 on 2021-05-06 16:11

import chat.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=chat.models.generate_unique_code, max_length=5, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
