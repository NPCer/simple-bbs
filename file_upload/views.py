from django.shortcuts import render, redirect
from .models import File
from django.urls import reverse
import os
import uuid
from django.conf import settings
from django.http import JsonResponse
from django.template.defaultfilters import filesizeformat
from django.contrib.contenttypes.models import ContentType
from post.models import LabPost
from .models import File


# Show file list
def file_list(request):
    files = File.objects.all().order_by("-id")
    return render(request, 'file_upload/file_list.html', {'files': files})


# Upload File with ModelForm
def model_form_upload(request):
    # 返回上传时的页面
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    if request.method == "POST":
        files = request.FILES.get('files', '')
        filename = request.POST.get('filename', '')
        # 检验上传文件
        if not request.user.is_authenticated:
            return render(request, 'error.html', {'message': '用户未登陆orz', 'redirect_to': referer})
        if files == '':
            return render(request, 'error.html', {'message': '附件不能为空诶', 'redirect_to': referer})
        if filename == '':
            return render(request, 'error.html', {'message': '文件名不能为空诶', 'redirect_to': referer})

        ext = files.name.split('.')[-1].lower()
        if (ext not in ["jpg", "pdf", "png", 'gif']) or (files.size > settings.MAX_UPLOAD_SIZE):
            request.session['file_form_error'] = 'YES'
            return redirect(referer)
        else:
            request.session['file_form_error'] = 'NO'

        try:
            content_type = request.POST.get('content_type', '')
            object_id = int(request.POST.get('object_id', ''))
            model_class = ContentType.objects.get(
                model=content_type).model_class()
            model_obj = model_class.objects.get(pk=object_id)
        except Exception as e:
            return render(request, 'error.html', {'message': '附件对象不存在', 'redirect_to': referer})

        filer = File()
        filer.files = files
        print('我是名字')
        print(filer.files.url)
        filer.filename = filename
        filer.file_size = files.size
        filer.file_path = filer.files.url
        filer.user = request.user
        filer.content_object = model_obj
        filer.save()
    return redirect(referer)
