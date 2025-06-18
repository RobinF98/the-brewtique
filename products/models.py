from django.db import models
from django.forms import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid


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
    sku = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=254)
    description = models.TextField()

    size = models.PositiveIntegerField(null=True, blank=True)

    KILOGRAM = "kg"
    GRAM = "g"
    LITER = "L"
    MILLILITER = "mL"
    NO_UNIT = ""
    UNIT_CHOICES = {
        KILOGRAM: "kilogram",
        GRAM: "gram",
        LITER: "liter",
        MILLILITER: "milliliter",
        NO_UNIT: "no_unit",
    }
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default=NO_UNIT, blank=True)

    has_strength = models.BooleanField(default=False, blank=True,)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.PositiveBigIntegerField(null=True,
                                 blank=True, validators=[
                                     MaxValueValidator(5),
                                     MinValueValidator(1),
                                 ])
    strength = models.PositiveIntegerField(null=True,
                                   blank=True, validators=[
                                       MaxValueValidator(5),
                                       MinValueValidator(1),
                                   ])
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def clean(self, *args, **kwargs):
        # ensure strength and has_strength agree
        is_strength_valid = True if self.has_strength == bool(self.strength) else False
        if not is_strength_valid:
            raise ValidationError(f"Please set a strength value. Strength: {bool(self.strength)}. has_strength{self.has_strength}")

        # ensure that if the product has a size, it has a unit too.
        # if self.get_unit_display() != 'no_unit' and self.strength is not None:
        size_matches_unit = bool(self.unit) == bool(self.size)
        if not size_matches_unit:
            raise ValidationError("The unit value needs a corresponding size value (and vice versa)")
