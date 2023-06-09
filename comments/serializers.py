from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    '''
    Serializer class for comment data
    is_owner is a booling field for the user accessing
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'post', 'created_at', 'updated_at',
            'content', 'profile_id', 'profile_image',
        ]

class CommentDetailSerializer(CommentSerializer):
    '''
    adds the post id to the comment
    '''
    post = serializers.ReadOnlyField(source='post.id')