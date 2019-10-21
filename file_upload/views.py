from django.shortcuts import render, redirect
from .models import File
from .forms import FileUploadModelForm
from django.urls import reverse
import os
import uuid
from django.http import JsonResponse
from django.template.defaultfilters import filesizeformat


# Show file list
def file_list(request):
    files = File.objects.all().order_by("-id")
    return render(request, 'file_upload/file_list.html', {'files': files})


# Upload File with ModelForm
def model_form_upload(request):
    # 返回上传时的页面
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    print(referer)
    print(request.get_full_path)
    if request.method == "POST":
        file_form = FileUploadModelForm(request.POST, request.FILES)
        if file_form.is_valid():
            file_form.save()
            # 手动传错误信息，模版中判断显示
            request.session['file_form_error'] = 'NO'
            return redirect(referer)
        else:
            request.session['file_form_error'] = 'YES'
            return redirect(referer)
    file_form = FileUploadModelForm()
    return render(request, reverse('home'))
