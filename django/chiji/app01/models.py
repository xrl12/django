from DjangoUeditor.models import UEditorField
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)
    position = models.IntegerField(verbose_name='排序', default=0)

    class Meta:
        abstract = True


class Banner(BaseModel):
    img = models.ImageField(upload_to='media/banner/%Y/%m/%d')
    link = models.URLField(verbose_name='跳转地址')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.link


class Category(BaseModel):
    name = models.CharField(verbose_name='分类名字', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class BlogUser(AbstractUser):
    phone = models.CharField(verbose_name='用户', max_length=11, unique=True)

    def __str__(self):
        return self.phone


class Tag(BaseModel):
    name = models.CharField(verbose_name='标签', max_length=10)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(BaseModel):
    is_top = models.BooleanField(verbose_name='是否置顶', default=False)
    title = models.CharField(verbose_name='标题', max_length=50)
    nvum = models.IntegerField(verbose_name='浏览量', default=0)
    content = UEditorField(width=600, height=300, toolbars="full",
                           imagePath="news/%(basename)s_%(datetime)s.%(extname)s", filePath="files/")
    user = models.ForeignKey(to=BlogUser, on_delete=models.CASCADE)
    tag = models.ManyToManyField(to=Tag)
    cover = models.ImageField(verbose_name='封面图片', upload_to='article_cover/%Y/%m/%d',
                              default='article_cover/2020/12/12')

    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class AB(BaseModel):
    logo = models.ImageField(verbose_name='公司logo', upload_to='media/logo/%Y/%m/%d')
    link = models.URLField(verbose_name='跳转地址')

    class Meta:
        verbose_name = '广告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.link


class PingLun(BaseModel):
    content = models.CharField(verbose_name='评论', max_length=100)
    user = models.ForeignKey(to=BlogUser, on_delete=models.CASCADE)
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
