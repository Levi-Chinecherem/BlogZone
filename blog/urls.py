# blog/urls.py

from django.urls import path
from .views import * 

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('<int:pk>/like/', like_post, name='like_post'),
    path('<int:pk>/favorite/', favorite_post, name='favorite_post'),
    path('post/', post_blog, name='post_blog'), 
    path('<int:pk>/update/', update_post, name='update_post'),
    path('<int:pk>/delete/', delete_post, name='delete_post'),

    path('<int:pk>/add_comment/', add_comment, name='add_comment'),
    
]
