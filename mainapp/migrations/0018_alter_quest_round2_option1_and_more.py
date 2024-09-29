# Generated by Django 5.1 on 2024-09-29 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_rounds_round'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest_round2',
            name='option1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='quest_round2',
            name='option2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='quest_round2',
            name='option3',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='quest_round2',
            name='option4',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='rounds',
            name='round_name',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(default='', max_length=250),
        ),
    ]
