from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'username']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop('password') # Quitamos password de validated_data.
        user = self.Meta.model(**validated_data)
        user.set_password(password) # Incluimos el password hasheado en user.
        user.save()
        return user