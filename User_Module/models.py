from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    user_avatar = models.ImageField(null=True, blank=True, upload_to='user-avatar/')
    user_create_date = models.DateTimeField(auto_now=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.username} : {self.email}'


class OTPModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, unique=True)
    otp = models.CharField(max_length=10)


class RoleModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UserRoleModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    role = models.ForeignKey(RoleModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'role')

    def __str__(self):
        return f'{self.user.username} : {self.role.name}'


class TokenModel(models.Model):
    key = models.CharField(_("Key"), max_length=50, primary_key=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = get_random_string(50)
        return super().save(*args, **kwargs)
