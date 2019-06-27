"""Module docstring 1
"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
 PermissionsMixin


class UserManager(BaseUserManager):
    """class docs str

    Arguments:
        BaseUserManager {nnn} -- nnn
    """
    def create_user(self, email, password=None, **extra_fields):
        """Create Use

        Arguments:
            email {str} -- email

        Keyword Arguments:
            password {str} -- password (default: {None})
        """
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password):
        """Create superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model

    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
