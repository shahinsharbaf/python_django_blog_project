from django.urls import path
from posts import views


urlpatterns = [
    path('', views.index,name='posts'),
    path('<str:url_post>', views.posts_by_title),
]
