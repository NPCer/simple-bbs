from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse


def home(request):
    return render(request, 'home.html')


def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(request, username=username, password=password)
    # 退到之前的页面，如果获取不到跳到home
    referer = request.META.get('HTTP_REFERER',reverse('home'))
    if user is not None:
        auth.login(request, user)
        return redirect(referer)
    else:
        return render(request, 'error.html', {'message': '用户名或密码不正确','redirect_to':referer})
