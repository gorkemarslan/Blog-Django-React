from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    tag = serializers.CharField(source='tag.name', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'content', 'tag', 'status',)
