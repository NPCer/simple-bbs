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
    if request.method == "POST":
        form = FileUploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(referer)
    else:
        form = FileUploadModelForm()

    # return render(request, 'file_upload/upload_form.html', {'form': form,
    #                                                         'heading': 'Upload files with ModelForm'})
    return redirect(referer)
