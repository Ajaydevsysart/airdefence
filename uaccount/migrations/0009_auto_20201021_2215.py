# Generated by Django 2.2.6 on 2020-10-22 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uaccount', '0008_auto_20201019_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='extendeduser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contact_no', models.IntegerField()),
                ('Service_No', models.IntegerField(null=True)),
                ('Address', models.TextField(max_length=1000, null=True)),
                ('Rank', models.CharField(max_length=20, null=True)),
                ('Trade', models.CharField(max_length=20, null=True)),
                ('Section', models.CharField(max_length=20, null=True)),
                ('Unit', models.CharField(max_length=20, null=True)),
                ('Ip_NO', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
