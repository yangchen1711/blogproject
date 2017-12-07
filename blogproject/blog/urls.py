# coding:utf-8
from django.conf.urls import url

import views
# 告诉Django这个urls.py模块是属于blog应用的。即视图函数的命名空间。

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.detail, name='detail'),
]