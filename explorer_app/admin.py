from django.contrib import admin
from django.contrib import admin
from explorer_app.models import *


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(PostType)
class PostTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "type"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ("on_linkedin", "on_facebook", "on_instagram")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Comment._meta.get_fields()]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Like._meta.get_fields()]


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Follow._meta.get_fields()]


@admin.register(SavedPost)
class SavedPostAdmin(admin.ModelAdmin):
    list_display = [f.name for f in SavedPost._meta.get_fields()]


@admin.register(ReportPost)
class ReportPostAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ReportPost._meta.get_fields()]


@admin.register(ReportUser)
class ReportUserAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ReportUser._meta.get_fields()]


@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Download._meta.get_fields()]


@admin.register(Promotions)
class PromotionsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Promotions._meta.get_fields()]


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Advertisement._meta.get_fields()]


@admin.register(ContactedList)
class ContactedListAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ContactedList._meta.get_fields()]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Message._meta.get_fields()]

