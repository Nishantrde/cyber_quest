# Generated by Django 5.1 on 2024-09-28 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_round1_rules'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='spec',
            field=models.BooleanField(default=False),
        ),
    ]
