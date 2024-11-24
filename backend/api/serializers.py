#from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    ##Creo que esto que sigue no se esta usando, esto se valida en el modelo directamente
    ##Chequear cuando este aburrido 
    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email ya está en uso.")
        return value

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("Este nombre de usuario ya está en uso.")
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

    
class ResetPasswordRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.RegexField(
        regex=r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
        write_only=True,
        error_messages={'invalid': ('Password must be at least 8 characters long with at least one capital letter and symbol')})
    
    confirm_password = serializers.CharField(write_only=True, required=True)
    
class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['id', 'name','description']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'sport']
        #extra_kwargs = {'sport': {'write_only': True}}

class SkillRatingSerializer(serializers.ModelSerializer):
    skill_name = serializers.SerializerMethodField()
    class Meta:
        model = SkillRating
        fields = ['id', 'player', 'skill', 'skill_name', 'like_count', 'dislike_count', 'like', 'dislike']
        extra_kwargs = {
            'like_count' : {'read_only' : True},
            'dislike_count' : {'read_only' : True}
        }
        
    def get_skill_name(self, obj):
        return obj.skill.name  # Accede al nombre de la skill

class PlayerSerializer(serializers.ModelSerializer):
    sport = SportSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ['id', 'first_name', 'last_name', 'nick_name', 'user', 'sport']
        extra_kwargs ={'user': {'write_only':True }}

   
##class SkillSerializer(serializers.ModelSerializer):
     

