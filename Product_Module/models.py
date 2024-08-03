from django.db import models
from User_Module.models import UserModel


class CategoryModel(models.Model):
    category_title = models.CharField(max_length=150, verbose_name='عنوان دسته بندی')
    category_slug = models.SlugField(unique=True, allow_unicode=True, db_index=True, verbose_name='عنوان در url')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.category_title


class SubCategoryModel(models.Model):
    sub_category_title = models.CharField(max_length=150, verbose_name='عنوان زیر دسته')
    sub_category_parent = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, verbose_name='دسته بندی')
    sub_category_slug = models.SlugField(unique=True, allow_unicode=True, db_index=True, verbose_name='عنوان در url')

    class Meta:
        verbose_name = 'زیر دسته'
        verbose_name_plural = 'زیر دسته ها'

    def __str__(self):
        return self.sub_category_title


class ProductModel(models.Model):
    product_title = models.CharField(max_length=150, verbose_name='نام کالا')
    product_description = models.TextField(verbose_name='توضیحات کالا')
    product_price = models.IntegerField(verbose_name='قیمت کالا')
    product_create_date = models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد محصول')
    product_slug = models.SlugField(unique=True, allow_unicode=True, db_index=True, verbose_name='عنوان در url')

    # Product Category
    product_category = models.ForeignKey(SubCategoryModel, on_delete=models.CASCADE, verbose_name='دسته یندی کالا')

    # Product Discount
    product_discount = models.IntegerField(default=0, verbose_name='تخفیف کالا')
    product_discount_date = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ تخفیف کالا')

    # Product Image
    product_cover = models.ImageField(null=True, upload_to='product-cover/', verbose_name='عکس کالا')

    class Meta:
        verbose_name = 'کالا'
        verbose_name_plural = 'کالا ها'

    def __str__(self):
        return self.product_title


class ProductFeatureModel(models.Model):
    feature_title = models.CharField(max_length=150, verbose_name='نام ویژگی')
    feature_description = models.CharField(max_length=150, verbose_name='توضیح ویژگی')
    feature_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name='محصول')

    class Meta:
        verbose_name = 'ویژگی کالا'
        verbose_name_plural = 'ویژگی های کالا ها'

    def __str__(self):
        return f'{self.feature_title} : {self.feature_description}'


class ProductImagesModel(models.Model):
    product_img = models.ImageField(upload_to='product-images/', verbose_name='عکس کالا')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name='کالا')

    class Meta:
        verbose_name = 'عکس کالا'
        verbose_name_plural = 'عکس های کالا ها'

    def __str__(self):
        return f'عکس شماره {self.id} : {self.product.product_title}'


class ProductCommentModel(models.Model):
    comment_text = models.TextField(verbose_name='متن کامنت')
    comment_rating = models.IntegerField(verbose_name='امتیاز')
    comment_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name='محصول')
    comment_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='کاربر')
    comment_create_date = models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'

    def __str__(self):
        return f'{self.comment_product.product_title} : {self.comment_user.username}'
