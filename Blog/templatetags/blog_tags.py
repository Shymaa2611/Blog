from django import template
from ..models import postBlog
from django.db.models import Count

register = template.Library()
@register.simple_tag
def total_posts():
 return postBlog.objects.count()

@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts(count=5):
 latest_posts = postBlog.objects.order_by('-published')[:count]
 return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_comment(count=3):
    return postBlog.objects.annotate(
     total_comments=Count('comments')  
    ).order_by('-total_comments')[:count]
