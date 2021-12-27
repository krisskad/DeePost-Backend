from djoser.serializers import UserCreateSerializer
from accounts.models import UserAccount
# from django.contrib.auth import get_user_model
# User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = UserAccount
        fields = ['id', 'email', 'first_name', 'last_name', 'username', 'password']