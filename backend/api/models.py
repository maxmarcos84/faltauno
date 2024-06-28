from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
# Create your models here.

# en models.py


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('El usuario debe tener un email válido')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class PasswordReset(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Sport(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

class Skills(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='skills_sport')
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], default=1
    )


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE , related_name='player')
    sport = models.ManyToManyField(Sport)
    skills = models.ManyToManyField(Skills)
    

class SkillRating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ratings') #Related_name es para despues poder hacer user.ratings
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='ratings')
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE, related_name='ratings')
    

    



