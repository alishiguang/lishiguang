#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class Catagory(models.Model):
    """
    类目
    """
    name=models.CharField("类目",max_length=200)

    class Meta:
        verbose_name='类目'
        verbose_name_plural='类目'

    def __unicode__(self):
        return self.name

class Article(models.Model):
    """
    文章
    """
    catagory=models.ForeignKey(Catagory,verbose_name='类目')
    pic = models.ImageField('图片',upload_to='uploadImages')
    headline=models.CharField("标题",max_length=200)
    article=models.TextField("文章")
    pub_date=models.DateTimeField("发布日期")

    class Meta:
        verbose_name='文章'
        verbose_name_plural='文章'

    def __unicode__(self):
        return self.headline



