from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime


# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.first_name


class Seller(User):
    sRating = models.FloatField()


class Category(models.Model):
    CategoryId = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)


class Bidder(User):
    bRating = models.FloatField(default=0.0)


class Item(models.Model):
    ItemId = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    # foreign key to Seller
    SellerId = models.ForeignKey(Seller, on_delete=models.CASCADE)
    description = models.TextField()
    categoryIds = models.ManyToManyField(Category)
    BidderIds = models.ManyToManyField(Bidder, through='Bid')
    startDate = models.DateTimeField(default=timezone.now())
    endDate = models.DateTimeField()


class Bid(models.Model):
    BidId = models.PositiveIntegerField(primary_key=True)
    Ammount = models.DecimalField(max_digits=8, decimal_places=2)
    ItemId = models.ForeignKey(Item, on_delete=models.CASCADE)
    BidderId = models.ForeignKey(Bidder, on_delete=models.CASCADE)














