from django.contrib import admin
from .models import LabPost, LabPostType
# Register your models here.


@admin.register(LabPostType)
class LabPostTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


@admin.register(LabPost)
class LabPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_data', 'get_read_num',
                    'edited_data', 'post_type', 'id')
