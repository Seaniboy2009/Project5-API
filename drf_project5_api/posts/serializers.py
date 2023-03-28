from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    '''
    Serializer class for Post data
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image is larger than 2mb, please resize')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        return value


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'title', 'profile_id',
            'profile_image', 'advert_image', 'reality_image','location', 
            'franchisor', 'created_at', 'updated_at',
            'content', 
        ]

