from rest_framework import serializers
from .models import Post
from like.models import Like
from vote.models import VoteAlike, VoteNotAlike


class PostSerializer(serializers.ModelSerializer):
    '''
    Serializer class for Post data
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    alike_id = serializers.SerializerMethodField()
    not_alike_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    alikes_count = serializers.ReadOnlyField()
    not_alikes_count = serializers.ReadOnlyField()

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
    
    # Get the first like for the logged in user
    # and the current pos, there should only be 1
    # per user per post
    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None
    
    def get_alike_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            alike = VoteAlike.objects.filter(
                owner=user, post=obj
            ).first()
            return alike.id if alike else None
        return None
    
    def get_not_alike_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            not_alike = VoteNotAlike.objects.filter(
                owner=user, post=obj
            ).first()
            return not_alike.id if not_alike else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'title', 'profile_id', 'like_id',
            'profile_image', 'advert_image', 'reality_image','location', 
            'alike_id', 'not_alike_id', 'franchisor', 'created_at', 'updated_at',
            'content', 'likes_count', 'comments_count', 'alikes_count', 'not_alikes_count'
        ]

