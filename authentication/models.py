from django.db import models

# Create your models here.
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

from django.db import models
from django.contrib.auth.models import User


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'),
                                                   reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="DEEPOST"),
        # message:
        email_plaintext_message,
        # from:
        "deepost.0o0@gmail.com",
        # to:
        [reset_password_token.user.email]
    )


class ExtendUser(models.Model):
    base_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    date_of_birth = models.DateField(null=True)
    city = models.ForeignKey('explorer_app.City', on_delete=models.CASCADE)  # user_id
    state = models.ForeignKey('explorer_app.State', on_delete=models.CASCADE)  # user_id
    country = models.ForeignKey('explorer_app.Country', on_delete=models.CASCADE)  # user_id
    bio = models.CharField(max_length=140, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='post_images')  # BASE_DIR -> media -> post_images
    coins = models.IntegerField(default=0)
    rank = models.IntegerField(default=100)
    followings = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    total_images = models.IntegerField(default=0)
    total_videos = models.IntegerField(default=0)
    instagram_id = models.CharField(max_length=255, blank=True, null=True)
    facebook_id = models.CharField(max_length=255, blank=True, null=True)
    linkedin_id = models.CharField(max_length=255, blank=True, null=True)

    website_link = models.CharField(max_length=255, blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.base_user)
