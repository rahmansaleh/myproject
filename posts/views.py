from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def post_list(request):
    postlist = Post.objects.filter(draft=False)
    return render(request, 'home.html', {'postlist': postlist})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, draft=False)
    return render(request, 'detail.html', {'post': post})