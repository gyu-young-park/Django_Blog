from django.db import models
from taggit.managers import TaggableManager

##taggit을 사용하면 tag를 만들어준다. pip로 설치하자
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField()
    img = models.ImageField(upload_to='images/')
    dateCreate = models.DateTimeField(auto_now_add=True)
    category = TaggableManager()

    def __str__(self):
        return self.title