from rest_framework import serializers
from .models import VoteAlike, VoteNotAlike
from django.db import IntegrityError


class VoteAlikeSerializer(serializers.ModelSerializer):
    '''
    Serializer class for Like data
    '''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = VoteAlike
        fields = [
            'id', 'owner', 'post', 'created_at',
        ]
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'message': 'duplicate like'
            })

class VoteNotAlikeSerializer(serializers.ModelSerializer):
    '''
    Serializer class for Like data
    '''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = VoteNotAlike
        fields = [
            'id', 'owner', 'post', 'created_at',
        ]
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'message': 'duplicate like'
            })