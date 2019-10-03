from django.urls import path
from .views import post_list, post_detail, type_post

# start with post
urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:post_id>/', post_detail, name='post_detail'),
    path('type/<int:type_id>', type_post, name='type_post'),
]
