from django.shortcuts import render
from pure_pagination import PageNotAnInteger,Paginator

from .models import Category, Article, Img_Joke, Ab


# Create your views here.

def img(request):
    img_jokes = Img_Joke.objects.filter(is_delete=False).all()
    categorys = Category.objects.all()
    articles = Article.objects.filter(is_delete=False).all()
    abs = Ab.objects.filter(is_delete=False).all()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    arts = Img_Joke.objects.all()
    p = Paginator(arts, per_page=1, request=request)
    art = p.page(page)

    marketing_list = []
    hot_list = []
    # for arts in article.object_list:
    #     print(arts)
    for img_joke in img_jokes:
        if img_joke.marketing:
            marketing_list.append(img_joke)
        if img_joke.is_hot:
            hot_list.append(img_joke)

    for article in articles:
        if article.marketing:
            marketing_list.append(article)
        if article.is_hot:
            hot_list.append(article)

    ctx = {
        'img_jokes': img_jokes,
        'cageorys': categorys,
        'articles': articles,
        'marketing_article': marketing_list,
        'abs': abs,
        'hots': hot_list,
        'art':art
    }
    for arts in art.object_list:
        print(arts.image)
    return render(request, 'img.html', ctx)


def pic_detail(request, id):
    img_jokes = Img_Joke.objects.filter(is_delete=False).all()
    articles = Article.objects.filter(is_delete=False).all()
    abs = Ab.objects.filter(is_delete=False).all()
    imgs = Img_Joke.objects.filter(id=id).first()
    marketing_list = []
    hot_list = []
    for img_joke in img_jokes:
        if img_joke.marketing:
            marketing_list.append(img_joke)
        if img_joke.is_hot:
            hot_list.append(img_joke)

    for article in articles:
        if article.marketing:
            marketing_list.append(article)
        if article.is_hot:
            hot_list.append(article)
    ctx = {
        'marketing_article': marketing_list,
        'abs': abs,
        'hots': hot_list,
        'imgs': imgs,
        'img_jokes': img_jokes,
    }
    return render(request, 'picdetail.html', ctx)


def text(request):
    categorys = Category.objects.all()
    img_jokes = Img_Joke.objects.filter(is_delete=False).all()
    articles = Article.objects.filter(is_delete=False).all()
    abs = Ab.objects.filter(is_delete=False).all()
    marketing_list = []
    hot_list = []
    for img_joke in img_jokes:
        if img_joke.marketing:
            marketing_list.append(img_joke)
        if img_joke.is_hot:
            hot_list.append(img_joke)

    for article in articles:
        if article.marketing:
            marketing_list.append(article)
        if article.is_hot:
            hot_list.append(article)

    ctx = {
        'marketing_article': marketing_list,
        'abs': abs,
        'hots': hot_list,
        'img_jokes': img_jokes,
        'categorys': categorys,
        'articles': articles
    }
    return render(request, 'text.html', ctx)


def text_detail(request, id):
    categorys = Category.objects.all()
    img_jokes = Img_Joke.objects.filter(is_delete=False).all()
    articles = Article.objects.exclude(id=id).filter(is_delete=False).all()
    abs = Ab.objects.filter(is_delete=False).all()
    article = Article.objects.filter(is_delete=False, id=id).all()

    marketing_list = []
    hot_list = []
    for img_joke in img_jokes:
        if img_joke.marketing:
            marketing_list.append(img_joke)
        if img_joke.is_hot:
            hot_list.append(img_joke)

    for article in articles:
        if article.marketing:
            marketing_list.append(article)
        if article.is_hot:
            hot_list.append(article)

    ctx = {
        'marketing_article': marketing_list,
        'abs': abs,
        'hots': hot_list,
        'img_jokes': img_jokes,
        'categorys': categorys,
        'articles': articles,
        'article': article
    }
    return render(request, 'textdetail.html', ctx)
