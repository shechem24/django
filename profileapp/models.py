from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(    # 1:1 연결, foreign key
        User,                       # 연결 주체
        on_delete=models.CASCADE,   # User 삭제 시, 자동 삭제
        related_name='profile',     # User에서 .profile로 바로 사용 가능(ex. request.user.profile.nickname)
    )
    image = models.ImageField(
        upload_to = 'profile/',       # media/profile/에 이미지 저장
        null = True
    )
    nickname = models.CharField(max_length=20,
        unique=True,
        null=True
    )
    message = models.CharField(max_length=100, null=True)