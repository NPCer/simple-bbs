# Generated by Django 2.2.1 on 2019-10-02 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20190528_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='labpost',
            name='readed_num',
            field=models.IntegerField(default=0),
        ),
    ]