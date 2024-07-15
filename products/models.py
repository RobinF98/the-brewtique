from string import ascii_uppercase
from django.db import models
from django.forms import ValidationError
from django.utils.crypto import get_random_string
from django.core.validators import MaxValueValidator, MinValueValidator
import string


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, unique=True, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_strength = models.BooleanField(default=False, null=True, blank=True,)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=1, null=True,
                                 blank=True, validators=[
                                     MaxValueValidator(10),
                                     MinValueValidator(1),
                                 ])
    strength = models.DecimalField(max_digits=2, decimal_places=1, null=True,
                                   blank=True, validators=[
                                       MaxValueValidator(5),
                                       MinValueValidator(1),
                                   ])
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    stock_quantity = models.PositiveIntegerField(default=1, null=False, blank=False)

    def __str__(self):
        return self.name

    def create_sku(self,):
        # generate random unique SKU
        if not self.sku:
            self.sku = get_random_string(length=12, allowed_chars=ascii_uppercase + string.digits)

    # def validate_strength(self, *args, **kwargs):
    #     """
    #         Checks that strength field has a value if has_strength is True
    #     """
    #     if self.has_strength and not self.strength or not self.has_strength and self.strength:
    #         raise ValidationError("Please set a strength value")

    def clean(self, *args, **kwargs):
        # ensure strength and has_strength agree
        if self.has_strength and not self.strength or not self.has_strength and self.strength:
            raise ValidationError("Please set a strength value")

    def save(self, *args, **kwargs):
        while True:
            try:  # check sku uniqueness and regenerate if not unique
                self.create_sku()
            except ValidationError:
                continue
            break
        # if not self.strength and self.has_strength:
        #     raise ValidationError("Please set a strength value.")
        super().save(*args, **kwargs)
