from django.shortcuts import render
from home.models import Posts
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_posts = {
        'posts':Posts.objects.all()
    }
    return render(request,'posts/index.html',context=my_posts)

def posts_by_title(request,url_post):
    for post in Posts.objects.all():
        if str(post)==str(post):
            return render(request,'posts/one_post.html',context={'post':post})
    return HttpResponse('not found')