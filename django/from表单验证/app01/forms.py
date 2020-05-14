import re

from django import forms
from .models import User

# 验证手机号
def re_phone(phone):
    pattern = re.compile(r'^\d[134567890]\d{8,8}\d$')
    if not pattern.match(str(phone)):
        raise forms.ValidationError('手机号错误')
    if User.objects.filter(phone=phone).first():
        raise forms.ValidationError('手机号已经被注册')


class LoginForm(forms.Form):
    phone = forms.IntegerField(label='账号', required=True,
                               error_messages={
                                   'required': '手机号是必填的',
                                   'max_length': '长度是11位',
                                   'min_length': '长度是11位',
                                   'invalid': '必须输入数字'
                               })
    pwd = forms.CharField(label='密码', required=True, min_length=6, error_messages={
        'required': '密码是必填的',
        'min_length': '最小长度是6位'
    },widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    phone = forms.IntegerField(label='手机号', required=True, validators=[re_phone, ],
                               error_messages={
                                   'max_length': '手机号不合法',
                                   'min_length': '手机号不合法',
                                   'required': '这个是必填的',
                                   'invalid': '必须输入数字'
                               })
    pwd = forms.CharField(label='密码', min_length=6, required=True, error_messages={
        'min_length': '密码不能小于6位',
        'required': '这个是必填的'
    },widget=forms.PasswordInput())

    pwd1 = forms.CharField(label='密码', min_length=6, required=True, error_messages={
        'min_length': '密码不能小于6位',
        'required': '这个是必填的'
    },widget=forms.PasswordInput())
    choise = [
        ('吃饭', '吃饭'),
        ('喝酒', '喝酒'),
        ('打豆豆’', '打豆豆')
    ]
    happy = forms.ChoiceField(label='兴趣爱好', choices=choise, error_messages={
        'choices': '兴趣不合法'
    })
    gender = [
        (1, '男'),
        (2, '女'),
        (3, '就不告诉你')
    ]
    genders = forms.ChoiceField(label='性别', required=True, choices=gender, error_messages={
        'required': '这个是必填的',
        'choices': '性别不合法'
    })

    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        pwd = cleaned_data['pwd']
        pwd2 = cleaned_data['pwd1']
        print('我扎着')
        if pwd != pwd2:
            print('wozaizhe')
            raise forms.ValidationError('二次输入密码不匹配')
        return cleaned_data  # 注意此处一定要return clean_data,否则会报错
