from django.contrib import admin
from .models import UserModel, RoleModel, UserRoleModel


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


class RoleModelAdmin(admin.ModelAdmin):
    list_display = ['name']


class UserRoleModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'role']


admin.site.register(UserModel, UserModelAdmin)
admin.site.register(RoleModel, RoleModelAdmin)
admin.site.register(UserRoleModel, UserRoleModelAdmin)
