from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.shortcuts import reverse

CATEGORIES = (
    ('GR', 'Groceries'),
    ('GOUR', 'Gourmet'),
    ('BVR', 'Beverages'),
    ('HH', 'HouseHolds'),
    ('PF', 'PackagedFoods'),
    ('PC', 'PersonalCare'),

)


class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    dummyP = models.FloatField()
    disc = models.TextField()
    category = models.CharField(choices=CATEGORIES, max_length=5)
    image = models.ImageField(upload_to='Products')
    offer = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    mobile = models.IntegerField()

    def __str__(self):
        return self.name


STATUS = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the way', 'On the way'),
    ('Delivered', 'Delivered'),
    ('Canceled', 'Canceled'),
    ('Out for Delivery', 'Out for Delivery')
)


class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=50, choices=STATUS, default='pending')
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=300, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
# Create your models here.


# Create your models here.
