from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(email=self.normalize_email(email),
                username = username)

        user.set_password(password)
        user.save(using=self. db)
        return user

    def create_superuser(self, email, username,password):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            password=password)

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self. db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(verbose_name='last login',auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AccountManager()
    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True