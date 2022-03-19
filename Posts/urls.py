from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('timeline', views.posts, name ='Posts'),
    path('Post_detail/<p_id>', views.post_detail, name='postDetails'),
    path('Likes', views.like, name ="like"),
    path('dislikes', views.dislikes, name ="dislikes"),
    path('sub_category/<cat_id>', views.sub_category, name="sub_category"),
    path('unsub_category/<cat_id>', views.unsub_category, name="unsub_category")
]
