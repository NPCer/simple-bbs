from django.db import models
from django.contrib.auth.models import User
from read_statistics.models import ReadNumExpandMethod
from ckeditor.fields import RichTextField
# Create your models here.


class LabPostType(models.Model):
    type_name = models.CharField(max_length=17)

    def __str__(self):
        return self.type_name


class LabPost(models.Model, ReadNumExpandMethod):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    readed_num = models.IntegerField(default=0)
    title = models.CharField(max_length=30, default='在此输入贴子标题')
    content = RichTextField()
    post_type = models.ForeignKey(
        LabPostType, on_delete=models.DO_NOTHING, null=True)
    created_data = models.DateTimeField(auto_now_add=True)
    edited_data = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_data']


class UploadFile(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to = "uploads/%Y/%m")