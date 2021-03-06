# -*- coding:utf-8 -*-
from ..models import Post, Category, Tag
from django import template
from django.db.models.aggregates import Count

register = template.Library()

# 1.9之后可以用@register.simple_tag()


@register.assignment_tag()
def get_recent_post(num=3):
    return Post.objects.all().order_by('-create_time')[:num]


@register.assignment_tag()
def archives():
    return Post.objects.dates('create_time', 'month', order='DESC')


@register.assignment_tag()
def get_categories():
    # return Category.objects.all()
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


@register.assignment_tag()
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
