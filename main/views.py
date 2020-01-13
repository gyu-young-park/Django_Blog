from django.shortcuts import render
from .models import Post
# Create your views here.
# Create your views here.
def index(req):
    postAll = Post.objects.all()
    return render(req,'main/index.html',{
        'postAll' : postAll,
    })

def postdetail(req, pk):
    post = Post.objects.get(pk=pk)
    return render(req,'main/postdetail.html',{
        'post':post,
    })