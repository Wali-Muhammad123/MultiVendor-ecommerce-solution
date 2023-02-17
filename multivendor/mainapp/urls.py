from . import views 
from django.urls import path
from django.contrib.auth.views import LoginView
app_name='mainapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginview, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path(
        'product/<int:product_id>/',
        views.product,
        name='product'
    ),
    path('search/', views.search, name='search'),
    path('retailer/', views.RetailerView.as_view(), name='retailer'),
    path('profile/',views.profile,name='profile'),
    path('report/',views.report,name='report'),
]