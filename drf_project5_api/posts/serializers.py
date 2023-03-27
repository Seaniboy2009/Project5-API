from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    '''
    Serializer class for Post data
    '''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'advert_image', 'reality_image',
            'location', 'franchisor', 'created_at', 'updated_at',
            'content'
        ]

