from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from mainsite.models import Post


def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count)) + str(post.title) + "<br>")
        post_lists.append("<small>" + str(post.body.encode('utf-8')) + "</small><br><br>")
    return HttpResponse(post_lists)
