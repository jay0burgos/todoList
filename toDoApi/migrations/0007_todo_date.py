# Generated by Django 2.2 on 2020-10-18 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDoApi', '0006_remove_todo_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
