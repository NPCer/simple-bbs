from django.db import models
import os
import uuid
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

# 重命名上传文件名


def user_directory_path(instance, filename):
    return filename


class File(models.Model):
    content_type = models.ForeignKey(
        ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    files = models.FileField(upload_to=user_directory_path)
    filename = models.CharField(max_length=200, verbose_name="请输入文件名")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    upload_time = models.DateTimeField(auto_now_add=True)
    file_size = models.DecimalField(max_digits=10, decimal_places=0)
    file_path = models.CharField(max_length=500)

    class Meta:
        ordering = ['-upload_time']
