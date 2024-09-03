from django.shortcuts import render
from likes.models import *
from django.http import JsonResponse
from .kafka_producer import *
# Create your views here.
def Post_like(request,post_id):
    send_like_event(post_id)
    #post =Post.objects.get(id=post_id)
    #post.like+=1
    #post.save()
    return JsonResponse({'like':"incremented"})
