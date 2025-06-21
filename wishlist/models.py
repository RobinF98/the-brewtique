from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=False, null=True, on_delete=models.SET_NULL)
