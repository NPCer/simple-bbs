# Generated by Django 2.2.6 on 2019-10-23 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0002_auto_20191023_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_path',
            field=models.CharField(max_length=500),
        ),
    ]
