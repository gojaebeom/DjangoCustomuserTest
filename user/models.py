from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('이메일은 필수입니다.')
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

    def create_user(self, email, password, **kwargs):
        """
        일반 유저 생성
        """
        kwargs.setdefault('is_staff', False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        """
        관리자 유저 생성
        """
        kwargs.setdefault('is_staff', True)
        return self._create_user(email, password, **kwargs)


# User Model 제정의
class CustomUser(AbstractBaseUser):
        objects = CustomUserManager()
        email = models.EmailField(unique=True, verbose_name='이메일')
        name = models.CharField(max_length=20, verbose_name='이름')
        date_joined = models.DateTimeField(auto_now_add=True, verbose_name='가입일')
        is_active = models.BooleanField(default=True, verbose_name='활성화 여부')
        is_staff = models.BooleanField(default=False, verbose_name='관리자 여부')
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['name']

        def has_perm(self, perm, obj=None):
            return self.is_staff

        def has_module_perms(self, app_label):
            return self.is_staff
        
        


