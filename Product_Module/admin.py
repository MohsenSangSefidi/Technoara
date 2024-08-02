from django.contrib import admin
from .models import ProductModel, ProductFeatureModel, CategoryModel, SubCategoryModel


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['product_title', 'product_price', 'product_category']
    prepopulated_fields = {'product_slug': ['product_title']}


class ProductFeatureModelAdmin(admin.ModelAdmin):
    list_display = ['feature_title', 'feature_description', 'feature_product']


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['category_title']
    prepopulated_fields = {'category_slug': ['category_title']}


class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['sub_category_title']
    prepopulated_fields = {'sub_category_slug': ['sub_category_title']}


admin.site.register(ProductModel, ProductModelAdmin)
admin.site.register(ProductFeatureModel, ProductFeatureModelAdmin)
admin.site.register(CategoryModel, CategoryModelAdmin)
admin.site.register(SubCategoryModel, SubCategoryModelAdmin)
