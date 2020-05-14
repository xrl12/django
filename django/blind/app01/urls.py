from django.urls import path

from .views import RegisterView, index,LoginView,logout

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('index/', index, name='index'),
    path('logout/',logout,name='logout')

]
