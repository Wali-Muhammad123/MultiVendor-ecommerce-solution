from django.urls import path 
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/',views.edit_profile,name='edit_profile'),
    path('product/',views.product,name='product'),
    path('product/id/<int:id>/',views.product_detail,name='product_detail'),
]