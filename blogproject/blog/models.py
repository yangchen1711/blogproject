# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import markdown
from django.utils.html import strip_tags

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()

    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User)

    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    # 获取Post自己对应的URL
    def get_absolute_url(self):
        # print self.pk
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    # def save(self, *args, **kwargs):
    #     if not self.excerpt:
    #         md = markdown.Markdown(extensions=[
    #                                 'markdown.extensions.extra',
    #                                 'markdown.extensions.codehilite',
    #                                 ])
    #         self.excerpt = strip_tags(md.convert(self.body))[:10]
    #
    #     super(Post, self).save(*args, **kwargs)
