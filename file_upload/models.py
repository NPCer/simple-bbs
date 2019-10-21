from django.db import models
import os
import uuid

# Create your models here.
# Define user directory path


# 重命名上传文件名
def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    original_name = filename.split('.')[0]
    filename = '{}-{}.{}'.format(original_name, uuid.uuid4().hex[:10], ext)
    print(filename)
    return os.path.join("files", filename)


class File(models.Model):
    file = models.FileField(upload_to=user_directory_path, null=True)
    # filename = models.CharField(default=,max_length=200);
    # upload_method = models.CharField(
    #     max_length=20, verbose_name="Upload Method")
    filename = models.CharField(
        max_length=200, verbose_name="请输入文件名")
