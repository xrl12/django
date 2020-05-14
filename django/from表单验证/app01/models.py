from django.db import models

# Create your models here.
class User(models.Model):
    phone = models.CharField(verbose_name='手机号',max_length=11)
    pwd = models.CharField(verbose_name='密码',max_length=255)
    happys = (
        ('吃饭','吃饭'),
        ('喝酒','喝酒'),
        ('打豆豆','打豆豆')
    )
    happy = models.CharField(choices=happys,verbose_name='兴趣',max_length=10)
    genders = (
        ('1,','男'),
        ('2','女'),
        ('3','未知')
    )
    gender = models.CharField(choices=genders,verbose_name='性别',max_length=10)
