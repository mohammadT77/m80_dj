# Generated by Django 4.1.7 on 2023-02-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.TextField(blank=True, max_length='14', null=True),
        ),
    ]
