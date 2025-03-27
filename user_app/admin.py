from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserManager


from django.contrib import admin
from .models import User  # CustomUserManager emas, User modelini import qilish kerak

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'name', 'is_admin', 'is_teacher', 'is_student', 'is_active')

admin.site.register(User, CustomUserAdmin)  # CustomUserManager emas!
