from django.urls import path
from .views import index,list,show,LoginView,RegisterView,log_out,tag,commit,search
urlpatterns = [
    path('',index,name='index'),
    path('list/<int:id>/',list,name='list'),
    path('show/<int:id>/',show,name='show'),
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('logout/',log_out,name='logout'),
    path('tag/<int:id>/',tag,name='tag'),
    path('commit/<int:id>/',commit,name='commit'),
    path('search/',search,name='search')
]
