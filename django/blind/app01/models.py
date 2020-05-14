from django.db import models

# Create your models here.
class User(models.Model):
    create_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)
    username = models.CharField(verbose_name='用户名字',max_length=20)
    age = models.IntegerField(verbose_name='用户年龄',default=18)
    phone = models.CharField(verbose_name='手机号',max_length=11,unique=True)
    cover = models.FileField(verbose_name='用户头像')
    pwd = models.CharField(verbose_name='密码',max_length=255)
    gender = (
        ('1','男'),
        ('2','女')
    )
    genders = models.CharField(choices=gender,max_length=5)
    happy = models.CharField(verbose_name='用户爱好',max_length=20)
    is_delete = models.BooleanField(verbose_name='是否删除',default=False)
    position = models.IntegerField(verbose_name='排序',default=0)
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name




