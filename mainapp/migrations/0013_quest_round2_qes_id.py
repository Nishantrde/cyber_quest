# Generated by Django 4.2.10 on 2024-09-26 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_alter_quest_round2_ans'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest_round2',
            name='qes_id',
            field=models.IntegerField(default=0),
        ),
    ]
