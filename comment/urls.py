from django.urls import path
from .views import update_comment

# start with post
urlpatterns = [
    path('update_comment', update_comment, name='update_comment'),
]
