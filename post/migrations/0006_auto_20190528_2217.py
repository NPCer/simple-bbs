# Generated by Django 2.2.1 on 2019-05-28 14:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0005_auto_20190527_1109'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='LabPost',
        ),
        migrations.RenameModel(
            old_name='PostType',
            new_name='LabPostType',
        ),
    ]