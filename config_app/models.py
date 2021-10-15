from django.db import models


# Create your models here.
class Configuration(models.Model):
    app_name = models.CharField(max_length=255)
    app_logo = models.ImageField(upload_to='app_images', null=True, blank=True)  # BASE_DIR -> media -> post_images
    app_opener_gif = models.ImageField(upload_to='app_images', null=True, blank=True)  # BASE_DIR -> media -> post_images
    app_font_style = models.CharField(max_length=255,  null=True, blank=True)
    app_main_color = models.CharField(max_length=255,  null=True, blank=True)
    app_slogan = models.CharField(max_length=255,  null=True, blank=True)
    app_welcome_text = models.CharField(max_length=255, null=True, blank=True)
    app_tips_text = models.CharField(max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
