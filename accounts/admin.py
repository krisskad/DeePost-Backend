from django.contrib import admin
from django.contrib import admin
from accounts.models import UserAccount


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'coins', 'date_joined', 'total_images', 'total_videos')