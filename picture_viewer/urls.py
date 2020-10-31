from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from app import views

urlpatterns = [
    re_path('admin/list/(?P<picture_id>\d+)/', views.delete),
    path('admin/list/', views.admin_show_list, name='admin_list'),
    re_path(r'^admin/', views.admin_add_picture, name='admin'),
    re_path(r'', views.index, name='home'),
    path('admin/', admin.site.urls),
]
