from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    born_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[
        ('erkak', 'Erkak'),
        ('ayol', 'Ayol')
    ])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

