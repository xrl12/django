from django.urls import path

from .views import text,img,pic_detail,text_detail

urlpatterns = [
    path('text/', text,name='text'),
    path('pic-detail/<int:id>/',pic_detail,name='pic_detail'),
    path('img/',img,name='pic'),
    path('text-detail/<int:id>/',text_detail,name='text_detail')
]
