from django.db import models
from Product_Module.models import ProductModel
from User_Module.models import UserModel


class CartModel(models.Model):
    id = models.AutoField(primary_key=True, db_index=True, editable=False)
    detail = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(default=False, verbose_name='وضعیت پرداخت')
    paid_date = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    final_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت پرداخت شده')

    def __str__(self):
        return f"{self.id} : {self.user}"

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = "سبدهای خرید"


class CartItemModel(models.Model):
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name='محصول')
    count = models.IntegerField(default=0, verbose_name='تعداد')

    def __str__(self):
        return f"{self.cart} - {self.product}"

    class Meta:
        verbose_name = 'محصول سبد خرید'
        verbose_name_plural = "محصولات سبد های خرید"
