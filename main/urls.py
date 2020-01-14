from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('' ,views.index,name="index"),
    path('post/<int:pk>/' ,views.postdetail,name="postdetail"),
    path('post/create/' ,views.post_create,name="post-create"),
    path('post/<int:pk>/update' ,views.postdetail,name="post-update"),
    path('post/<int:pk>/delete' ,views.postdetail,name="post-delete"),
    path('login/' ,views.signin,name="login"),
    path('logout/' ,views.siginout,name="logout"),
]