from django.contrib import admin
from .models import Profile

admin.site.register(Profile)




"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

# Делаем профиль "встройкой" для страницы юзера
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'
    fields = ("first_name", "last_name")

# Настраиваем стандартную админку юзеров
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

# Перерегистрируем
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

"""
