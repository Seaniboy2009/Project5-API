from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    '''
    Serializer class for Post data
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'title', 'advert_image', 'reality_image',
            'location', 'franchisor', 'created_at', 'updated_at',
            'content', 'is_owner'
        ]

