from django.shortcuts import render

def post(req):
    return render(req,'post/post.html')