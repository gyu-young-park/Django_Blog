from django.shortcuts import render , redirect , HttpResponse
from .models import Post
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate ,logout
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

def signin(req):
    if req.method == "POST":
        form = UserForm(req.POST)
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(req,user)
            return redirect('/')
        else:
            return HttpResponse('로그인 실패, 다시 시도해보세요')
    else:
        form = UserForm()
        return render(req,'main/login.html',{
            'form' : form,
        })

def siginout(req):
    logout(req)
    req.session.flush()
    return redirect('/')