# Generated by Django 3.2.4 on 2021-07-31 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createtodo',
            name='Date',
            field=models.DateField(default='2021-07-31'),
        ),
        migrations.AlterField(
            model_name='createtodo',
            name='Time',
            field=models.TimeField(default='09:09:09'),
        ),
    ]
