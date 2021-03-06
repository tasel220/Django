from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tags.models import Tag
# Create your models here.

# Create your models here.
class Post(models.Model): # 모델 클래스명은 단수형을 사용 (Posts(x) Post(O))
# id는 자동 추가
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    def update_date(self): # 나중에 수정할 때 사용
        self.updated_at = timezone.now()
        self.save()
    def __str__(self):
        return self.title
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(User, blank=True, related_name='like_posts', through='Like')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now) 
 
    def __str__(self):
        return f'[post: {self.post}] {self.content}'
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE) 

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)