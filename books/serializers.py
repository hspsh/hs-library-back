from django.contrib.auth.models import User
from rest_framework import serializers

from . import models


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'title', 'description', 'allowed_to_lend', 'tags', 'owner']
        read_only_fields = ('id', 'owner',)
        model = models.Book

    def create(self, validated_data):
        request_user = self.context['request'].user.id
        tags = validated_data.pop('tags')
        validated_data['owner_id'] = request_user
        instance = models.Book.objects.create(**validated_data)
        instance.tags = tags
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    """
    ``Serializer`` for ``User`` ..
    """

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'is_active', 'is_staff')
        read_only_fields = ('is_active', 'is_staff')
        extra_kwargs = {
            'security_question': {'write_only': True},
            'security_question_answer': {'write_only': True},
            'password': {'write_only': True}
        }
