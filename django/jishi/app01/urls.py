from django.urls import path

from . import views
urlpatterns = [
    path('users/',views.UserList.as_view(),),
    path('users/<int:id>/',views.UserDetail.as_view()),
    path('shops/',views.ShopList.as_view()),
    path('shops/<int:id>/',views.ShopDetail.as_view())
]
