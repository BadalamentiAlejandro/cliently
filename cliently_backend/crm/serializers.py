from rest_framework import serializers
from .models import Client, Comment
from django.contrib.auth import get_user_model


User = get_user_model()


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name']
        read_only_fields = ['id']
        extra_kwargs = {'name': {'required': True}}


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'client', 'user', 'text', 'date']
        read_only_fields = ['id', 'date', 'client', 'user']
        extra_kwargs = {'text': {'required': True}}