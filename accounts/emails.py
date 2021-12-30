from templated_mail.mail import BaseEmailMessage
from django.contrib.auth.tokens import default_token_generator
from djoser import utils
from djoser.conf import settings


class ActivationEmail(BaseEmailMessage):
    template_name = "email/activation.html"

    def get_context_data(self):
        # ActivationEmail can be deleted
        context = super().get_context_data()

        user = context.get("user")
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.ACTIVATION_URL.format(**context)
        context["domain"] = "deepost-0o0.web.app"  # Your site domain
        context["protocol"] = "https"  # Your site protocol e.g. ("http", "https")
        return context
