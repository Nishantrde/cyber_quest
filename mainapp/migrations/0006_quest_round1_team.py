# Generated by Django 4.2.10 on 2024-09-20 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_rename_team_team_team_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest_round1',
            name='team',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='mainapp.team'),
            preserve_default=False,
        ),
    ]
