from django.urls import path,register_converter

from .views import index1,index2,index3,index4,index5,index6
from .converters import PhoneConverter
register_converter(PhoneConverter,'phone')
urlpatterns = [
    # path('<int:id>/', index1),
    # path('<str:name>/',index2),
    # path('<path:url>/',index3),
    # path('<uuid:id>/',index4),
    # path('<slug:str>/',index5),
    path('<phone:sj>/',index6)
]


# from django.urls import path, register_converter
#
# from . import converters, views
# register_converter(converters.PhoneConverter,'phone')
# # register_converter(converters.PhoneConverter, 'yyyy')
#
# urlpatterns = [
#     path('articles/2003/', views.special_case_2003),
#     path('<phone:year>/', views.index6),
#     path('<phone:sj>/',views.index6)
# ]