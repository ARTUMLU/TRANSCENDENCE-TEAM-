from django.urls import path, include
from . import views, admin
from .views import upload_file_view ,list_users_view, new_funcation

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('', views.home_view, name='home'),
    path('success/', views.new_funcation, name='success'),
    path('upload/', upload_file_view, name='upload_file'),
    path('list-users/', list_users_view, name='list_users'),
]
