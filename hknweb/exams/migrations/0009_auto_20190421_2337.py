# Generated by Django 2.1.7 on 2019-04-21 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0008_auto_20190421_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=4, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='subject',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
