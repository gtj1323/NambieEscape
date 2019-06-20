from django.db import models
from django.conf import settings # 유저모델을 가져오는 것.
from django.contrib.auth.models import AbstractUser # 커스텀 유저 모델

# Create your models here.
class Calendar(models.Model):
    type = models.CharField(max_length = 50)
    title = models.TextField()
    content = models.TextField(blank=True)
    date = models.DateTimeField()
    term = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    def __str__(self):
        return self.title