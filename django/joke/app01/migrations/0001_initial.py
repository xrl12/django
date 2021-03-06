# Generated by Django 2.1.5 on 2020-03-21 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('name', models.CharField(max_length=20, verbose_name='公司名字')),
                ('logo', models.ImageField(upload_to='logo/ab')),
                ('expire', models.DateTimeField(verbose_name='过期时间')),
                ('link', models.URLField(default='https://www.baidu.com/', verbose_name='点击链接')),
            ],
            options={
                'verbose_name': '广告',
                'verbose_name_plural': '广告',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('name', models.CharField(max_length=50, verbose_name='笑话名字')),
                ('marketing', models.BooleanField(default=False, verbose_name='是否推介')),
                ('is_hot', models.BooleanField(default=False, verbose_name='是否热门')),
                ('content', models.TextField(verbose_name='内容')),
                ('is_top', models.IntegerField(default=0, verbose_name='顶一下')),
                ('is_step', models.IntegerField(default=0, verbose_name='踩一下')),
            ],
            options={
                'verbose_name': '笑话文章',
                'verbose_name_plural': '笑话文章',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('name', models.CharField(max_length=10, verbose_name='分类名字')),
                ('position', models.IntegerField(default=0, verbose_name='排序')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Img_Joke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('image', models.FileField(upload_to='joke_img/%Y/%m/%d')),
                ('name', models.CharField(default='默认笑话名字', max_length=50, verbose_name='笑话名字')),
                ('marketing', models.BooleanField(default=False, verbose_name='是否推介')),
                ('is_top', models.IntegerField(default=0, verbose_name='顶一下')),
                ('is_step', models.IntegerField(default=0, verbose_name='踩一下')),
                ('is_hot', models.BooleanField(default=False, verbose_name='是否热门')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Category', verbose_name='外键')),
            ],
            options={
                'verbose_name': '图片笑话文章',
                'verbose_name_plural': '图片笑话文章',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Category', verbose_name='外键'),
        ),
    ]
