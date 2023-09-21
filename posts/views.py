from django.shortcuts import render
from home.models import Posts
from django.http import Http404

# Create your views here.

def index(request):
    my_posts = {
        'posts':Posts.objects.all()
    }
    return render(request,'posts/index.html',context=my_posts)

def posts_by_title(request,slug):
    try:
        my_post = Posts.objects.get(slug=slug)
        # my_post=next(post for post in Posts.objects.all() if str(post)==str(url_post))
    except:
        raise Http404()
    else:
        return render(request,'posts/one_post.html',context={'post':my_post})
    