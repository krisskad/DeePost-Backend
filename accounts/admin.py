from django.contrib import admin
from django.contrib import admin
from accounts.models import UserAccount

from rest_framework_simplejwt import token_blacklist


class OutstandingTokenAdmin(token_blacklist.admin.OutstandingTokenAdmin):

    def has_delete_permission(self, *args, **kwargs):
        return True # or whatever logic you want

admin.site.unregister(token_blacklist.models.OutstandingToken)
admin.site.register(token_blacklist.models.OutstandingToken, OutstandingTokenAdmin)


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'coins', 'date_joined', 'total_images', 'total_videos')