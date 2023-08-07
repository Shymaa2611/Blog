from django.shortcuts import get_object_or_404, render
from .models import postBlog
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .forms import postForm,commentForm
from django.core.mail import send_mail
from django.conf import settings
def list_post(request):
    post=postBlog.objects.all()
    paginator = Paginator(post, 3) 
    page = request.GET.get('page')
    try:
     posts = paginator.page(page)
    except PageNotAnInteger:
       posts = paginator.page(1)
    except EmptyPage:
      posts = paginator.page(paginator.num_pages)
    return render(request,'blog/list.html',{'page':page,'posts':posts})


def detail_post(request,id):
    post=postBlog.objects.get(id=id)
    comments=post.comments.filter(active=True)
    new_comment=None
    if request.method=='POST':
       form=commentForm(request.POST)
       if form.is_valid():
          new_comment=form.save(commit=False)
          new_comment.post=post
          new_comment.save()
    else:
       form=commentForm()
    context={
       'post':post,
       'comments':comments,
       'form':form,
       'new_comment':new_comment
    }
       
    return render(request,'blog/detail.html',context)
    

def share_post(request,id):
   #post = get_object_or_404(postBlog, id=id, status='published')
   post=postBlog.objects.get(id=id)
   sent=False
   #post_url = request.build_absolute_uri(post.get_absolute_url())
   if request.method=='POST':
      form=postForm(request.POST,request.FILES)
      if form.is_valid():
         data= form.cleaned_data
         subject = f"{data['name']} recommands you to read this post {post.title}"
         message = f"Read {post.title} \n\n {data['name']} comments: {data['comments']}"
         from_email = settings.EMAIL_HOST_USER
         recipient_list = [data['email_to']]
         send_mail(subject, message, from_email, recipient_list,fail_silently=False)
         sent=True

   else:
      form=postForm()
   context={
      'form':form,
      'sent':sent,
      'post':post 
    }
   return render(request,'blog/share.html',context)
