import re

from django import forms
from django.forms import ValidationError


def re_phone(phone):
    if not re.match(r'^\d[13456789]\d{8,8}\d$', phone):
        raise ValidationError('手机号不合法')


def re_email(email):
    if not re.match(r'^\w+(@qq.com|@163.com)$', email):
        raise ValidationError('邮箱不合法，我们只支持qq邮箱和163邮箱')


class RegisterForm(forms.Form):
    phone = forms.CharField(max_length=11, min_length=11, required=True, validators=[re_phone, ], label='手机号',
                            error_messages={'max_length': '长度必须是十一位',
                                            'min_length': '长度必须是十一位',
                                            'required': '该字段是必填的'})
    pwd = forms.CharField(required=True, label='密码', min_length=6,
                          error_messages={
                              'min_length': '该字段的最小长度是6位',
                              'required': '该字段是必填的'
                          }, widget=forms.PasswordInput)

    pwd2 = forms.CharField(required=True, label='密码', min_length=6,
                           error_messages={
                               'min_length': '该字段的最小长度是6位',
                               'required': '该字段是必填的'
                           }, widget=forms.PasswordInput
                           )

    user_name = forms.CharField(required=True, label='用户名', min_length=2, max_length=10,
                                error_messages={
                                    'required': '这个是必填的',
                                    'min_length': '最小长度是2',
                                    'max_length': '最大长度是10',
                                })
    email = forms.CharField(label='邮箱', required=True, min_length=6, max_length=20,validators=[re_email,],
                            error_messages={
                                'required': '这个是必填的',
                                'min_length': '这个字段的最小长度是6',
                                'max_lnegth': '这个字段的最高长度是20'
                            })

    def clean(self):
        pwd = self.cleaned_data.get('pwd')
        pwd2 = self.cleaned_data.get('pwd2')
        print(pwd,pwd2)
        print(self.cleaned_data)
        if not pwd == pwd2:
            print('wozaizheli')
            raise ValidationError('两次秘密输入不一致')
        return self.cleaned_data


class LoginForm(forms.Form):
    phone = forms.CharField(max_length=11, min_length=11, required=True, validators=[re_phone, ], label='手机号',
                            error_messages={'max_length': '长度必须是十一位',
                                            'min_length': '长度必须是十一位',
                                            'required': '该字段是必填的'})
    pwd = forms.CharField(required=True, label='密码', min_length=6,
                          error_messages={
                              'min_length': '该字段的最小长度是6位',
                              'required': '该字段是必填的'
                          }, widget=forms.PasswordInput)
