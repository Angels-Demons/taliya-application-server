from django.contrib import admin
from django.contrib.auth import get_user_model

from accounts.models import Profile

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ('phone', 'is_active', 'is_admin', 'is_staff', 'timestamp')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email')


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
