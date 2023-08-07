from django.db import models
from django.contrib.auth.models import User
class postBlog(models.Model):
    STATUS={
        ('draft','Draft'),
        ('publish','Publish')
    }
    title=models.CharField(max_length=100)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    published=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=STATUS,max_length=10)
    class Meta:
        ordering=('-published',)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post=models.ForeignKey(postBlog,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField()
    content=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
    class Meta:
        ordering = ('create_at',)
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'