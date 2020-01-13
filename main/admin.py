from django.contrib import admin
from .models import Post
#admin페이지 커스터마이징 클래스
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','dateCreate')
admin.site.register(Post , PostAdmin)