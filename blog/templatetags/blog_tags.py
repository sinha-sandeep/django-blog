from blog.models import Post
from django import template
register=template.Library()
from django.db.models import Count

@register.simple_tag
def total_post():
    return Post.objects.count()

@register.inclusion_tag("blog/latest_post123.html")
def show_latest_post():
    latest_post=Post.objects.order_by('-publish')[:5]
    return{'latest_post':latest_post}



@register.filter
def most_commented_post(count=5):
    return Post.objects.annotate(most_comment=Count('comments')).order_by('-most_comment')[:count]
