from rest_framework import serializers
from .models import Post

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'points', 'date_posted', 'author')