from django import forms
from django.contrib.auth.models import User
from main.models import Post
from django.utils.translation import gettext_lazy as _

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'contents','img','category']
        labels = {
            'title' : _('제목'),
            'contents' : _('내용'),
            'img': _('사진'),
            'category': _('카테고리'),
        }
        help_text = {
            'title' : _("제목을 입력해주세요"),
            'contents': _("내용을 입력해주세요"),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username' , 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }