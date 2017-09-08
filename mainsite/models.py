# coding:utf-8
from __future__ import unicode_literals    #  为了兼容python2 ① 这个必须放在第一行
from django.db import models
# Create your models here.
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible       #  为了兼容python2 ②


@python_2_unicode_compatible                #  为了兼容python2 ③
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title
