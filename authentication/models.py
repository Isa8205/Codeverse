from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class Users(AbstractUser):
    gender = models.CharField(max_length=20, null=False, default='Prefer not to say')
    profile = models.FileField(upload_to='Profiles/', default='profiles/avatar1.png')
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.username}"

    @property
    def full_name(self):
        return f"{super.firstname} {self.lastname}"

    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return None