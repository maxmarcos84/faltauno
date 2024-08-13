from django.shortcuts import render
#from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage
from .models import *
import os

from django.contrib.auth import get_user_model
User = get_user_model()
        
class CreateUserView(generics.CreateAPIView):    
    #queryset = User.objects.all()
    serializer_class = CustomUserSerializer 
    permission_classes = [AllowAny] 

class RequestPasswordReset(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResetPasswordRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        email = request.data['email']
        user = User.objects.filter(email__iexact=email).first()

        if user:
            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(user) 
            reset = PasswordReset(email=email, token=token)
            reset.save()

            ##reset_url = f"{os.environ['PASSWORD_RESET_BASE_URL']}/{token}"
            reset_url = "api/user/reset_password/{token}"

            # Sending reset link via email (commented out for clarity)           

            email = EmailMessage(
                "Recuperacion de contraseña FaltaUno",
                "Para recuperar la contraseña del usuario {user.username} dirijase a este link: {reset_url}",                
                to=["marcoss.ridao@gmail.com"]                
            )
            email.send()

            # ... (email sending code)

            return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "User with credentials not found"}, status=status.HTTP_404_NOT_FOUND)

class ResetPassword(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = []

    def post(self, request, token):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        
        new_password = data['new_password']
        confirm_password = data['confirm_password']
        
        if new_password != confirm_password:
            return Response({"error": "Passwords do not match"}, status=400)
        
        reset_obj = PasswordReset.objects.filter(token=token).first()
        
        if not reset_obj:
            return Response({'error':'Invalid token'}, status=400)
        
        user = User.objects.filter(email=reset_obj.email).first()
        
        if user:
            user.set_password(request.data['new_password'])
            user.save()
            
            reset_obj.delete()
            
            return Response({'success':'Password updated'})
        else: 
            return Response({'error':'No user found'}, status=404)
        

class CreatePlayerView(generics.CreateAPIView):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny] #Habilitado para pruebas

class UpdatePlayerView(generics.UpdateAPIView):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
    permission_classes = [AllowAny] #Habilitado para pruebas


class SkillsRatingCreateView(generics.CreateAPIView):
    serializer_class = SkillRatingSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny] #Habilitado para pruebas
    pass

class SkillRatingUpdateView(generics.UpdateAPIView):
    serializer_class = SkillRatingSerializer
   
class GetPlayersByUserView(generics.ListAPIView):
    serializer_class = PlayerSerializer
    ##permission_classes  = [IsAuthenticated]
    permission_classes = [AllowAny] #Habilitado para pruebas

    def get_queryset(self):
        return Player.objects.filter(user = self.kwargs['user_id'])
    
    
class getSportsView(generics.ListAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer    
    ##permission_classes  = [IsAuthenticated]
    permission_classes = [AllowAny] #Habilitado para pruebas

class GetSkillsBySport(generics.ListAPIView):
    serializer_class = SkillSerializer
    ##permission_classes  = [IsAuthenticated]
    permission_classes = [AllowAny] #Habilitado para pruebas

    def get_queryset(self):
        return Skill.objects.filter(sport = self.kwargs['sport_id'])


