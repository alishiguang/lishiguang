#-*- coding:utf-8 -*-
__author__ = 'Lishiguang'

from django.contrib import admin
from lishiguang.cms.models import Catagory, Article

page_sie = 2

class ArticleAdmin(admin.ModelAdmin):
    list_per_page = page_sie #分页条数
    list_display = ('headline', 'catagory', 'pub_date')
    list_filter = ('pub_date', 'catagory')
    ordering = ('-pub_date',)

    class Media:
        js = ('/site_media/js/tiny_mce/tiny_mce.js', '/site_media/js/textareas.js')

admin.site.register(Catagory)
admin.site.register(Article, ArticleAdmin)
