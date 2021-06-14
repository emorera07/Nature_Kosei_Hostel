from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models herre

class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser):
        if not email:
            raise ValueError('Se requiere una direccion email valida')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password):
        return self._create_user(email, password, False, False)

    def create_superuser(self, email, password):
        user=self._create_user(email, password, True, True)
        return user


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    is_staff = models.BooleanField(null=False)

    def say_hello(self):
        return "Hello,{}".format(self.username)
    
    #def save(self, commit=True):
        #user = None 
     #   User = super(User, self).save(commit=False) 
     #   User.email = self.cleaned_data["email"] 
     #   if commit: 
      #      User.save() 
       # return User 

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username


    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    #@property
    #def is_staff(self):
     #   return self.staff
