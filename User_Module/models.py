from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    user_avatar = models.ImageField(null=True, blank=True, upload_to='user-avatar/', verbose_name='عکس کاربر')
    user_create_date = models.DateTimeField(auto_now=True, verbose_name='تاریخ عضویت')
    user_verify_code = models.IntegerField(null=True, blank=True, verbose_name='کد تایید')
    user_token = models.CharField(null=True, blank=True, max_length=150, verbose_name='توکن')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return f'{self.username} : {self.email}'
