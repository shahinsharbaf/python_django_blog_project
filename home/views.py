from django.shortcuts import render
from .models import Posts

# Create your views here.
def home(request):
    my_posts = {
        'posts':Posts.objects.all()
    }
    return render(request,'home/index.html',context=my_posts)