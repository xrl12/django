from django.contrib.auth import logout
from django.contrib.auth.backends import ModelBackend
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from pure_pagination import Paginator, PageNotAnInteger


from .form import LoginForm, RegisterForm
from .models import Banner, Article, Category, Tag, BlogUser, AB, PingLun


# Create your views here.
def index(request):
    banners = Banner.objects.filter(is_delete=False).all()
    articles = Article.objects.filter(is_delete=False).all()
    categorys = Category.objects.filter(is_delete=False).all()
    uid = request.COOKIES.get('uid')
    user = BlogUser.objects.filter(id=uid).first()
    abs = AB.objects.filter(is_delete=False).all()

    commit = PingLun.objects.filter(is_delete=False).all()
    art_id = []
    art_conetn = []
    for com in commit:
        if com.article.id not in art_id:
            art_id.append(com.article.id)
    for arts in art_id:
        art = Article.objects.filter(id=arts).all()
        art_conetn.extend(art)
    if not user:
        user = None
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    # arts = Article.objects.all()
    p = Paginator(articles, per_page=1, request=request)
    article = p.page(page)
    return render(request, 'index.html', locals())


def list(request, id):
    uid = request.COOKIES.get('uid')
    user = BlogUser.objects.filter(id=uid).first()
    commit = PingLun.objects.filter(is_delete=False).all()
    art_id = []
    art_conetn = []
    for com in commit:
        if com.article.id not in art_id:
            art_id.append(com.article.id)
    for arts in art_id:
        art = Article.objects.filter(id=arts).all()
        art_conetn.extend(art)
    if not user:
        user = None
    abs = AB.objects.filter(is_delete=False).all()
    tags = Tag.objects.filter(is_delete=False).all()

    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return render(request, '404.html')

    if not category:
        return render(request, '404.html', locals())
    articles = category.article_set.all()

    return render(request, 'list.html', locals())


def tag(request, id):
    uid = request.COOKIES.get('uid')
    user = BlogUser.objects.filter(id=uid).first()
    category = Tag.objects.filter(is_delete=False, id=id).first()
    tags = Tag.objects.filter(is_delete=False).all()
    commit = PingLun.objects.filter(is_delete=False).all()
    art_id = []
    art_conetn = []
    for com in commit:
        if com.article.id not in art_id:
            art_id.append(com.article.id)
    for arts in art_id:
        art = Article.objects.filter(id=arts).all()
        art_conetn.extend(art)
    if not user:
        user = None
    if not category:
        return render(request, '404.html')
    articles = category.article_set.all()
    return render(request, 'list.html', locals())


def show(request, id):
    uid = request.COOKIES.get('uid')
    user = BlogUser.objects.filter(id=uid).first()
    abs = AB.objects.filter(is_delete=False).all()

    article = Article.objects.filter(id=id).first()
    articles = Article.objects.all()
    commits = PingLun.objects.filter(article=id).order_by('create_time').all()
    commit = PingLun.objects.filter(is_delete=False).all()
    art_id = []
    art_conetn = []
    for com in commit:
        if com.article.id not in art_id:
            art_id.append(com.article.id)
    for arts in art_id:
        art = Article.objects.filter(id=arts).all()
        art_conetn.extend(art)

    # print(art_conetn)

    if not user:
        user = None
    if not article:
        return render(request, '404.html')
    tuijie = article.category.article_set.exclude(id=id).all()
    article.nvum += 1
    article.save()

    return render(request, 'show.html', locals())


class LoginView(View, ModelBackend):
    def authenticate(self, request, phone=None, password=None, **kwargs):
        try:
            user = BlogUser.objects.get(phone=phone)
            if user.check_password(password):
                return user
        except Exception as e:
            return None

    def get(self, request):
        loginform = LoginForm()
        return render(request, 'login.html', locals())

    def post(self, request):

        loginform = LoginForm(request.POST)
        ctx = {
            'loginform': loginform,
        }
        if loginform.is_valid():
            phone = loginform.cleaned_data.get('phone')
            pwd = loginform.cleaned_data.get('pwd')
            user = self.authenticate(request, phone, pwd)
            ctx = {
                'error': '账号或者密码错误',
                'loginform': loginform,
            }
            if user:
                response = redirect(reverse('app01:index'))
                response.set_cookie('uid', user.id)
                return response
            return render(request, 'login.html', ctx)
        return render(request, 'login.html', ctx)


class RegisterView(View):
    def get(self, request):
        registerform = RegisterForm()
        return render(request, 'register.html', locals())

    def post(self, request):
        registerform = RegisterForm(request.POST)
        if registerform.is_valid():
            pwd = registerform.cleaned_data.get('pwd')
            phone = registerform.cleaned_data.get('phone')
            username = registerform.cleaned_data.get('user_name')
            email = registerform.cleaned_data.get('email')
            BlogUser.objects.create_user(phone=phone, password=pwd, username=username, email=email)
            return redirect(reverse('app01:login'))
        else:
            return render(request, 'register.html', locals())


@csrf_exempt
def search(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        article = Article.objects.filter(Q(title__icontains=keyword)|Q(content__icontains=keyword))
        if not article:
            return render(request, '404.html', locals())
        return redirect(reverse('app01:list' ,kwargs={'id': 1}))


def log_out(request):
    logout(request)
    response = redirect(reverse('app01:index'))
    response.delete_cookie('uid')
    return response


def commit(request, id):
    ctx = {}
    user = request.COOKIES.get('uid')
    if not user:
        ctx['error'] = '请先进行登录'
        return redirect(reverse('app01:show', kwargs={'id': id}), ctx)
    else:
        commit = request.POST.get('comment-textarea')
        user = BlogUser.objects.get(id=user)
        article = Article.objects.get(id=id)
        print('-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o->', commit)
        PingLun.objects.create(user=user, article=article, content=commit)
        return render(request, 'show.html', locals())
