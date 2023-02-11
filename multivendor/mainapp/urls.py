from .views import *
from django.urls import path
from django.conf.urls import url
app_name = 'mainapp'
urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path(
        'product/<int:product_id>/',
        product,
        name='product'
    ),
]