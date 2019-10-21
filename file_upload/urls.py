from django.urls import re_path, path
from . import views

# namespace
app_name = "file_upload"

urlpatterns = [

    # Upload Files Using Model Form
    path('upload/', views.model_form_upload, name='model_form_upload'),

    # View File List
    path('', views.file_list, name='file_list'),
    path('up/',views.model_form_upload),

]
