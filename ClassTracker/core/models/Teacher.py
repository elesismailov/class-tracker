from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )

        return self._create_user(email, password, **extra_fields)


class Teacher(AbstractUser):

    first_name   = models.CharField(max_length=20)
    second_name  = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, unique=True)
    subject_name = models.CharField(max_length=50)


    USERNAME_FIELD = "phone_number" # make the user log in with the email
    REQUIRED_FIELDS = ["username", 'email']

    objects = CustomUserManager()

    def name(self):
        return self.first_name + ' ' + self.second_name

    def __str__(self):
        return self.name() + ' ' + self.phone_number

