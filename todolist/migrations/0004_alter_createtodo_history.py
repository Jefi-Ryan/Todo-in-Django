# Generated by Django 3.2.4 on 2021-07-31 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_auto_20210731_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createtodo',
            name='History',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
    ]
