from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    user_avatar = models.ImageField(null=True, blank=True, upload_to='user-avatar/', verbose_name='عکس کاربر')
    user_create_date = models.DateTimeField(auto_now=True, verbose_name='تاریخ عضویت')
    user_verify_code = models.IntegerField(null=True, blank=True, verbose_name='کد تایید')
    user_token = models.CharField(null=True, blank=True, max_length=150, verbose_name='توکن')
    email = models.EmailField(unique=True, verbose_name='ایمیل')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return f'{self.username} : {self.email}'

    def user_avatar_url(self):
        try:
            return f'http://127.0.0.1:8000/{self.user_avatar.url}'
        except:
            return ''


class RoleModel(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'نقش'
        verbose_name_plural = 'نقش ها'

    def __str__(self):
        return self.name


class UserRoleModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    role = models.ForeignKey(RoleModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'نقش کاربر'
        verbose_name_plural = 'نقش های کاربران'
        unique_together = ('user', 'role')

    def __str__(self):
        return f'{self.user.username} : {self.role.name}'

