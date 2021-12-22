from django.contrib import admin
from django.contrib import admin
from accounts.models import UserAccount


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    pass