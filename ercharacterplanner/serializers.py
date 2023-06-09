from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import (
    Armament,
    Armament_Slot,
    CustomUser,
    Character,
    Character_Armament,
    Character_Attribute,
    Main_Attribute,
    Starting_Class,
    Starting_Class_Attribute
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

class ArmamentSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    data = serializers.JSONField()

    class Meta:
        model = Armament
        fields = ('id', 'name', 'data')

class MainAttributeSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Main_Attribute
        fields = ('id', 'name')

class CharacterAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character_Attribute
        fields = ('id', 'character', 'attribute', 'value')

class CharacterAttributeReadSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='main_attribute.id')
    name = serializers.ReadOnlyField(source='main_attribute.name')

    class Meta:
        model = Character_Attribute
        fields = ('id', 'name', 'value')

class CharacterArmamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character_Armament
        fields = ('id', 'character', 'armament', 'slot')

class CharacterArmamentReadSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='armament.id')
    name = serializers.ReadOnlyField(source='armament.name')

    class Meta:
        model = Character_Armament
        fields = ('id', 'name', 'slot')

class CharacterWriteSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=16)

    class Meta:
        model = Character
        fields = ('id', 'name', 'starting_class', 'owner')

class CharacterReadOnlySerializer(serializers.ModelSerializer):
    leveled_attributes = CharacterAttributeReadSerializer(source='character_attribute_set', many=True)
    armaments = CharacterArmamentReadSerializer(source='character_armament_set',many=True)

    class Meta:
        model = Character
        fields = (
            'id', 
            'name', 
            'starting_class', 
            'leveled_attributes',
            'armaments', 
            'owner'
        )

class StartingClassAttributeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='main_attribute.id')
    name = serializers.ReadOnlyField(source='main_attribute.name')

    class Meta:
        model = Starting_Class_Attribute
        fields = ('id', 'name', 'base_value')

class StartingClassSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    attributes = StartingClassAttributeSerializer(source='starting_class_attribute_set' , many=True)

    class Meta:
        model = Starting_Class
        fields = ('id', 'name', 'attributes')
