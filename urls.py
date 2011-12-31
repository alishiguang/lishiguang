#-*- coding:utf-8 -*-
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #富文本框
    (r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root': 'media'}),
    # Example:
    # (r'^lishiguang/', include('lishiguang.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #后台管理
    (r'^admin/', include(admin.site.urls)),
    #首页
    (r'^$','cms.views.index'),
)
