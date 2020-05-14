from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm
from .models import User


# Create your views here.
def register(request):
    if request.method == 'POST':
        register = RegisterForm(request.POST)
        ctx = {
            'register': register
        }
        if register.is_valid():
            phone = register.cleaned_data.get('phone')
            pwd = register.cleaned_data.get('pwd')
            happy = register.cleaned_data.get('happy')
            genders = register.cleaned_data.get('genders')
            User.objects.update_or_create(
                phone=phone,
                pwd=pwd,
                happy=happy,
                gender=genders
            )
        return redirect(reverse('login'))

    else:
        register = RegisterForm()
        ctx = {
            'register': register
        }
        return render(request, 'register.html', ctx)


def login(request):
    loginform = LoginForm(request.POST)
    ctx = {'loginform': loginform}
    if request.method == 'POST':
        print('我这这里')
        if loginform.is_valid():
            phone = loginform.cleaned_data.get('phone')
            pwd = loginform.cleaned_data.get('pwd')

            print(phone,pwd)
            user = User.objects.filter(phone=phone, pwd=pwd).first()
            if user:
                response = HttpResponse('登陆成功')
                response.set_cookie('uid',user.id)
                return response
    return render(request, 'login.html', ctx)
