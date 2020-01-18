from django.contrib import admin
from django.urls import path ,include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include('main.urls')),
    path('about/', include('about.urls')),
    path('contact/',include('contact.urls')),
    path('post/',include('post.urls')),
    url(r'^markdownx/', include('markdownx.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
