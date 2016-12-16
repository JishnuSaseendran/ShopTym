from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.item_list, name='item_list'),
    url(r'^register/$', views.register, name='register'),
    url(r'^item/(?P<pk>\d+)/$', views.item_detail, name='item_detail'),
    url(r'^item/new/$', views.item_new, name='item_new'),
    url(r'^item/(?P<pk>\d+)/edit/$', views.item_edit, name='item_edit'),
    url(r'^drafts/$', views.item_draft_list, name='item_draft_list'),
    url(r'^item/(?P<pk>\d+)/publish/$', views.item_publish, name='item_publish'),
    url(r'^item/(?P<pk>\d+)/remove/$', views.item_remove, name='item_remove'),
]
