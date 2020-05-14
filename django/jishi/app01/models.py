from django.db import models

# Create your models here.
class User(models.Model):
    account = models.IntegerField(verbose_name='用户账号')
    password = models.CharField(verbose_name='密码',max_length=255)
    phone = models.IntegerField(verbose_name='手机号',max_length=11)
    name = models.CharField(verbose_name='用户名字',max_length=20)
class Shop(models.Model):
    name = models.CharField(verbose_name='商品名字',max_length=20)
    price = models.IntegerField(verbose_name='价格',)
    is_show = models.BooleanField(verbose_name='是否显示',default=True)


