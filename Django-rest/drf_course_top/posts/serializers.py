from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedIdentityField(view_name='user-detail')

    class Meta:
        model = Post
        fields = ('title', 'category', 'publish_date', 'last_updated', 'author')



class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = User
            fields = ('id')