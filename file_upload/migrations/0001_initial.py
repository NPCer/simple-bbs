# Generated by Django 2.2.6 on 2019-10-23 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import file_upload.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('files', models.FileField(upload_to=file_upload.models.user_directory_path)),
                ('filename', models.CharField(max_length=200, verbose_name='请输入文件名')),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('file_size', models.DecimalField(decimal_places=0, max_digits=10)),
                ('file_path', models.CharField(max_length=500)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-upload_time'],
            },
        ),
    ]
