from django.db import models
from django.utils import timezone
from User_Module.models import UserModel


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250, verbose_name='نام')
    cover_img = models.ImageField(upload_to='blog_cover/', verbose_name='عکس کاور', null=True)
    slug = models.SlugField(max_length=250, unique=True, verbose_name='عنوان در url')
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='نویسنده')
    body = models.TextField(verbose_name='متن')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='زمان آپدیت')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published', verbose_name='وضعیت')

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return self.title

    def cover_img_url(self):
        return f'http://localhost:8000{self.cover_img.url}'
