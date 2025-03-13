from django.urls import path
from . import views

app_name = 'users' # boshqa app ichida ishlatganimiz uchun

urlpatterns = [
    path('', views.home_view, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]