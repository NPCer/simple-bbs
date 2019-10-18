# Generated by Django 2.2.6 on 2019-10-17 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='upload_method',
        ),
        migrations.AddField(
            model_name='file',
            name='filename',
            field=models.CharField(default='请输入文件名', max_length=200, verbose_name='Upload Method'),
        ),
    ]