from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 数字路由
def index1(request,id):
    print(id)
    return HttpResponse('OK')

# 字符串路由
def index2(request,name):
    print(name)
    return HttpResponse('OK')

# 路径路由
def index3(request,url):
    # 和字符串路由基本没有什么区别，唯一的区别就是他可以匹配/而字符串路由不可以
    print(url)
    return HttpResponse('OK')

# uuid路由
def index4(request,url):
    print(url)
    return HttpResponse('OK')

# slug路由
def index5(request,str):
    print(str)
    return HttpResponse('OK')

# 自定义路由
def index6(request,sj):
    print(sj)
    return HttpResponse('Ok')


