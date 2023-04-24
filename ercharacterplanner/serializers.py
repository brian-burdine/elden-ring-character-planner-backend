from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import (
    CustomUser,
    Character
)

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class CharacterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=16)

    class Meta:
        model = Character
        fields = ('id', 'name', 'owner')