# Generated by Django 2.1.5 on 2020-03-18 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('username', models.CharField(max_length=20, verbose_name='用户名字')),
                ('age', models.IntegerField(default=18, verbose_name='用户年龄')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='手机号')),
                ('cover', models.FileField(upload_to='', verbose_name='用户头像')),
                ('pwd', models.CharField(max_length=255, verbose_name='密码')),
                ('genders', models.CharField(choices=[('1', '男'), ('2', '女')], max_length=5)),
                ('happy', models.CharField(max_length=20, verbose_name='用户爱好')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('position', models.IntegerField(default=0, verbose_name='排序')),
            ],
            options={
                'verbose_name_plural': '用户',
                'verbose_name': '用户',
            },
        ),
    ]
