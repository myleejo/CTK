from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.




class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    
class User(AbstractUser):
    nickname = models.CharField(max_length=24, unique=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=False)
    # 추가 필드 등 다른 설정들을 여기에 추가할 수 있습니다
    
    # USERNAME_FIELD를 'email'로 설정
    USERNAME_FIELD = 'email'
    # email을 REQUIRED_FIELDS에서 제거
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email 
    objects = CustomUserManager()