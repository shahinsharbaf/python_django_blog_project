from django.urls import path
from posts import views


urlpatterns = [
    path('', views.index,name='posts'),
    path('<slug:slug>', views.posts_by_title),
]
