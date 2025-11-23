from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

# UserProfile admin
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')  # show user and role in admin
    search_fields = ('user__username', 'role')  # search by username or role
