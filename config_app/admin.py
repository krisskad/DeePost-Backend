from django.contrib import admin
from django.contrib import admin
from config_app.models import Configuration


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    exclude = ("app_opener_gif", "app_logo", "app_font_style", "app_main_color")