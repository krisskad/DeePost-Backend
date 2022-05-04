from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from accounts.models import UserAccount
from accounts.serializers import UserCreateSerializer

from explorer_app.models import (
    Post,
    PostImage,
    PostType,
    User
)
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class PostTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostType
        fields = ['type', ]


class PostImageSerializer(serializers.ModelSerializer):
    original_url = serializers.ImageField()

    class Meta:
        model = PostImage
        fields = '__all__'


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'email', 'first_name', 'last_name', 'username')


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    user = GetUserSerializer(read_only=True)
    images = PostImageSerializer(many=True)
    post_type = PostTypeSerializer()
    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = ['user','images', 'post_type', 'tags',
                  'total_likes',
                  'total_comments',
                  'total_downloads',
                  'total_views',
                  'total_likes',
                  'total_likes',
                  'public',
                  'deleted',
                  'archived',
                  'on_instagram',
                  'on_facebook',
                  'on_linkedin',
                  'created_on',
                  'updated_on'
                  ]


class CreatePostSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = User
        fields = ('id', 'post')

#
# class ArticleSerializer(WritableNestedModelSerializer):
#     image_large = serializers.ImageField(read_only=True)
#     image_medium = serializers.ImageField(read_only=True)
#     image_small = serializers.ImageField(read_only=True)
#     image_tag = serializers.ImageField(read_only=True)
#
#     class Meta:
#         model = PostImage
#         fields = [
#             'created_at',
#             'updated_at',
#             'created_by',
#             'title',
#             'slug',
#             'image',
#             'image_large',
#             'image_medium',
#             'image_small',
#             'image_tag',
#             'description',
#         ]