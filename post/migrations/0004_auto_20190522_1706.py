# Generated by Django 2.2.1 on 2019-05-22 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20190522_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='post.PostType'),
        ),
    ]
