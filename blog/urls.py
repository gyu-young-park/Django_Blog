from django.contrib import admin
from django.urls import path
from main.views import index, postdetail
from about.views import about
from post.views import post
from contact.views import contact
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/',about , name='about'),
    path('post/',post ,name='post'),
    path('post/<int:pk>/',postdetail ,name='detail'),
    path('contact/',contact ,name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
