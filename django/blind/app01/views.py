import hashlib
import os
import re
from datetime import datetime
from random import randint

from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.views import View

from .models import User


# Create your views here.


def get_md5(pwd):
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf8'))
    return md5.hexdigest()


def re_phoen(phone):
    pattern = re.compile(r'^\d[134567890]\d{8,8}\d$')
    return pattern.match(phone)


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')

    def post(self, request, *args, **kwargs):
        ctx = {}
        IMG = ['png', 'jpeg', 'jpg']
        phone = request.POST.get('phone')
        pwd = request.POST.get('pwd')
        pic = request.FILES.get('pic')
        age = request.POST.get('age')
        pwd2 = request.POST.get('pwd2')
        happys = request.POST.getlist('happy')
        username = request.POST.get('username')
        user_gender = request.POST.get('gender')
        print(pic, phone, pwd, age, happys, user_gender)
        if User.objects.filter(phone=phone).first():
            ctx['error'] = '手机号已经被注册'
            return render(request, 'register.html', ctx)
        if not user_gender in ['男', '女', '保密']:
            ctx['error'] = '性别不合法'
            return render(request, 'register.html', ctx)
        if len(username) < 2 or len(username) > 20:
            ctx['error'] = '用户名不合法'
            return render(request, 'register.html', ctx)

        if not re_phoen(phone):
            ctx['error'] = '手机号不合法'
            return render(request, 'register.html', ctx)

        if not pwd == pwd2:
            ctx['error'] = '两次密码不正确'
            return render(request, 'register.html', ctx)

        for happy in happys:
            if happy not in happys:
                ctx['error'] = '爱好不合法'
                return render(request, 'register.html', ctx)

        try:
            print(pic)

            postfix = str(pic).split('.')[-1]
            if postfix not in IMG:
                print('我在这里')
                ctx['error'] = '图片只支持(png,jpeg,jpg)'
                print('我错了')
                return render(request, 'register.html', ctx)

            else:
                media_root = settings.MEDIA_ROOT
                path = 'news/{}/{}/{}/'.format(datetime.now().year, datetime.now().month, datetime.now().day)
                full_path = media_root + '/' + path
                print(full_path)
                if not os.path.exists(full_path):
                    os.makedirs(full_path)
                print('我错了嘛')
                # print(full_path+pic)
                with open(full_path + str(pic), 'wb') as pics:
                    print('不，我没有错')
                    for c in pic.chunks():
                        print('我错了')
                        pics.write(c)
                        print('我没有错')
        except:
            ctx['error'] = '图片不合法'
            return render(request, 'register.html', ctx)

        User.objects.create(
            phone=phone,
            username=username,
            pwd=get_md5(pwd),
            happy=','.join(happys),
            genders=user_gender,
            cover=path + str(pic),
            age=age,
        ).save()
        return redirect(reverse('app01:login'))


class LoginView(View):
    def get(self, request, *args, **kwargs):
        code = randint(1000, 9999)
        print(code)
        request.session['code'] = code
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        ctx = {}
        yzm = request.POST.get('code')
        phone = request.POST.get('phone')
        pwd = request.POST.get('pwd')
        code = request.session.get('code')
        password = get_md5(pwd)
        print(yzm, code)
        if not str(code) == str(yzm):
            ctx['error'] = '验证码失效'
            return render(request, 'login.html', ctx)
        print(password, phone)
        user = User.objects.filter(phone=phone, pwd=password).first()
        if not user:
            ctx['error'] = '账号或者密码错误'
            return render(request, 'login.html', ctx)
        response = redirect(reverse("app01:index"))
        response.set_cookie('uid', user.id, max_age=24 * 60 * 60)
        return response


def index(request):
    ctx = {'user': None}
    uid = request.COOKIES.get('uid')
    print('我着这里')
    if not uid:
        print('我走着列')
        ctx['error'] = '请您先登录在进行访问'
        return render(request, 'index.html', ctx)
    try:
        user = User.objects.get(id=uid)
    except:
        ctx['error'] = '没有这个用户'
        return render(request, 'index.html', ctx)

    happy = user.happy
    ctx = {'user': user}
    print('-------------->’', happy)
    for happys in happy.split(','):
        re_user = User.objects.exclude(genders=user.genders).filter(happy__contains=happys).all()
        print('----------->', re_user)
    return render(request, 'index.html', locals())


def logout(request):
    request.session.delete('uid')
    ctx = {'user': None}
    return render(request, 'index.html', ctx)
