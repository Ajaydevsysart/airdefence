# Generated by Django 2.2.6 on 2020-10-20 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uaccount', '0007_auto_20201019_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Address',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
