from django.db import models
from django.contrib.auth.models import AbstractUser

class Member(AbstractUser):
    residence = models.CharField(max_length=200, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    is_member = models.BooleanField(default=False)
    is_treasurer = models.BooleanField(default=False)
    is_storekeeper = models.BooleanField(default=False)
    is_secretary = models.BooleanField(default=False)
    is_troop_leader = models.BooleanField(default=False)
    is_scoutmaster = models.BooleanField(default=False)
