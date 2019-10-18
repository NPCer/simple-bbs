from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse
from .forms import LoginForm


def home(request):
    return render(request, 'home.html')


# 如果是post就处理登陆表单并返回到跳转页面
# 如果是get就显示登陆表单模版并跳转到首页
def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 具体的登陆检验在form中处理好了
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        login_form = LoginForm()
    context = {}
    context['login_form'] = login_form
    return render(request, 'login.html', context)
