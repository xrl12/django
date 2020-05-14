from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class BaseModel(models.Model):
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(verbose_name='分类名字', max_length=10)
    position = models.IntegerField(verbose_name='排序', default=0)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(BaseModel):
    name = models.CharField(verbose_name='笑话名字', max_length=50)
    marketing = models.BooleanField(verbose_name='是否推介', default=False)
    is_hot = models.BooleanField(verbose_name='是否热门', default=False)
    content = models.TextField(verbose_name='内容')
    is_top = models.IntegerField(verbose_name='顶一下', default=0)
    is_step = models.IntegerField(verbose_name='踩一下', default=0)
    category = models.ForeignKey(verbose_name='外键',on_delete=models.CASCADE,to=Category)
    # Contents = UEditorField(width=600, height=300, toolbars="full",
    #                        imagePath="news/%(basename)s_%(datetime)s.%(extname)s", filePath="files/",null=True,blank=True)

    class Meta:
        verbose_name = '笑话文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Img_Joke(BaseModel):
    image = models.FileField(upload_to='joke_img/%Y/%m/%d')
    name = models.CharField(verbose_name='笑话名字', max_length=50, default='默认笑话名字')
    marketing = models.BooleanField(verbose_name='是否推介', default=False)
    is_top = models.IntegerField(verbose_name='顶一下', default=0)
    is_step = models.IntegerField(verbose_name='踩一下', default=0)
    is_hot = models.BooleanField(verbose_name='是否热门', default=False)
    category = models.ForeignKey(verbose_name='外键', on_delete=models.CASCADE, to=Category)
    class Meta:
        verbose_name = '图片笑话文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Ab(BaseModel):
    name = models.CharField(verbose_name='公司名字', max_length=20)
    logo = models.ImageField(upload_to='logo/ab')
    expire = models.DateTimeField(verbose_name='过期时间')
    link = models.URLField(verbose_name='点击链接',default='https://www.baidu.com/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '广告'
        verbose_name_plural = verbose_name
