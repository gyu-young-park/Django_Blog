from django.shortcuts import render , redirect , HttpResponse , HttpResponseRedirect , get_object_or_404
from .models import Post
from .forms import UserForm , PostForm
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate ,logout
# Create your views here.
# Create your views here.
def index(req):
    postAll = Post.objects.all().select_related().order_by('-dateCreate')
    return render(req,'main/index.html',{
        'postAll' : postAll,
    })

def postdetail(req, pk):
    post = Post.objects.get(pk=pk)
    return render(req,'main/postdetail.html',{
        'post':post,
    })

def post_create(req):
    if req.method == 'POST':
        ##image는 files로 온다
        form = PostForm(req.POST, req.FILES)
        print(form)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/')
    form = PostForm()
    return render(req, 'main/post_create.html',{
        'form' : form,
    })

def post_update(req):
    if req.method == 'POST':
        post = get_object_or_404(Post,pk=req.POST.get('id'))
        form = PostForm(req.POST , instance=post)
        if form.is_valid():
            item = form.save()
    elif req.method == 'GET':
        post = get_object_or_404(Post,pk=req.GET.get('id'))
        form = PostForm(instance=post)
        return render(req, 'main/post_update.html', {
            'form' : form,
        })
    return redirect('index')

def post_delete(req,pk):
    post = get_object_or_404(Post,pk=pk)
    post.delete()
    return HttpResponseRedirect('/')


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