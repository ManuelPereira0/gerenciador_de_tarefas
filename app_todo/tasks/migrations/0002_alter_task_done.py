# Generated by Django 4.2.4 on 2023-08-29 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.CharField(choices=[('doing', 'Fazendo'), ('done', 'Feito')], max_length=7),
        ),
    ]
