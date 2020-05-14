from django.contrib import admin
from .models import Category,Article,Ab,Img_Joke
# Register your models here.

admin.site.register(Ab)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Img_Joke)

