# Generated by Django 2.2.6 on 2020-10-19 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uaccount', '0005_auto_20201019_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airman',
            name='Series_No',
        ),
        migrations.AddField(
            model_name='airman',
            name='Service_No',
            field=models.IntegerField(null=True),
        ),
    ]
