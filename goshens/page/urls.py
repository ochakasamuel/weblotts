from django.conf.urls import url
from . import views


app_name = 'page'

urlpatterns = [

    url(r'^category/(?P<category_slug>[\w-]+)/$', views.post_by_category, name='post_by_category'),
    url(r'^(?P<id>[0-9]+)/$', views.page_detail, name='page_detail'),
    url(r'^$', views.index_list, name='index_list'),


]
