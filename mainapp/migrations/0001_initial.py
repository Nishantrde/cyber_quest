# Generated by Django 4.2.10 on 2024-09-15 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quest_round1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest', models.CharField(max_length=250)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]
