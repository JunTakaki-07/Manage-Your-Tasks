# Generated by Django 3.0.5 on 2020-05-04 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tm_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myassignment',
            name='task_description',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='myassignment',
            name='task_purpose',
            field=models.TextField(max_length=100),
        ),
    ]