# Generated by Django 4.2.4 on 2023-09-04 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.CharField(choices=[('to do', 'Fazer'), ('doing', 'Fazendo'), ('done', 'Feito')], max_length=7),
        ),
    ]
