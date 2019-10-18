from django.shortcuts import render, get_object_or_404
from .models import LabPost, LabPostType
from django.db import connection
from django.contrib.contenttypes.models import ContentType
from read_statistics.utils import read_statistics_once_read
from comment.models import Comment
from file_upload.models import File
from file_upload.forms import FileUploadModelForm
# Create your views here.

# 返回指定类型贴子简要（默认返回全部）


def post_list(request):
    context = {}
    context['posts'] = LabPost.objects.filter(is_delete=False)
    context['post_types'] = LabPostType.objects.all()
    context['post_types_id'] = []
    # context['user'] = request.user
    # 判断是否有传入type，返回指定类型贴子
    if 'type' in request.GET.keys():
        post_types = []
        # print(request.GET.getlist('type'))
        post_types = request.GET.getlist('type')
        # print(post_types)
        # ['1', '2']
        # 返回所有在这个type中的post
        context['posts'] = LabPost.objects.filter(
            post_type__in=LabPostType.objects.filter(id__in=post_types))
        # 返回指定type的id，方便默认勾选
        context['post_types_id'] = post_types
    connection.close()
    return render(request, 'post/post_list.html', context)


# 返回指定id贴子内容
def post_detail(request, post_id):
    post = get_object_or_404(LabPost, id=post_id)
    read_cookie_key = read_statistics_once_read(request, post)
    post_content_type = ContentType.objects.get_for_model(post)
    comments = Comment.objects.filter(
        content_type=post_content_type, object_id=post.pk)

    context = {}
    context['post'] = post
    context['comments'] = comments
    # 处理上传附件
    files = File.objects.all().order_by("-id")
    context['files'] = files
    context['form'] = FileUploadModelForm()
    
    connection.close()
    response = render(request, 'post/post_detail.html', context)
    response.set_cookie(read_cookie_key, 'true')

    return response


# 返回指定类型下的所有贴子简要
def type_post(request, type_id):
    context = {}
    post_type = get_object_or_404(LabPostType, id=type_id)
    context['post_types'] = LabPostType.objects.all()
    context['posts'] = LabPost.objects.filter(
        post_type=post_type,)
    context['type_name'] = post_type.type_name
    connection.close()
    return render(request, 'post/type_post.html', context)
