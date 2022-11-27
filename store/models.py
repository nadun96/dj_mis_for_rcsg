from __future__ import _Feature
from django.db import models
from django.contrib.auth.models import User
# Create your models here


class Items(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=True)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    unit_price = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    date_received = models.DateField(auto_now_add=True)
    expiry_date = models.DateField(auto_now_add=False)
    is_purchased = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Broken(models.Model):
    id = models.ForeignKey(
        Items, to_field='id', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    unit_price = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    date_received = models.DateField(auto_now_add=True)
    expiry_date = models.DateField(auto_now_add=False)
    is_purchased = models.BooleanField(default=True)

    def __str__(self):
        return self.item.name


class Lends(models.Model):
    date = models.DateField(auto_now_add=True)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    to = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    reason = models.CharField(max_length=100)
    due_date = models.DateField(verbose_name='due date')

    ITEM_STATUS_CHOICES = {
        ('1', 'Good Condition'), ('2', 'Broken')
    }

    status = models.models.CharField(
        max_length=50, choices=ITEM_STATUS_CHOICES, default='1')

    def __str__(self):
        return self.item.name


class Returns(models.Model):
    date = models.DateField(auto_now_add=True)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    fine = models.DecimalField(
        verbose_name='fine', default='', decimal_places=6)
    ITEM_STATUS_CHOICES = {
        ('1', 'Good Condition'), ('2', 'Broken')
    }

    def calculate_fine():
        pass

    status = models.models.CharField(
        max_length=50, choices=ITEM_STATUS_CHOICES, default='1')

    def __str__(self):
        return self.item.name
