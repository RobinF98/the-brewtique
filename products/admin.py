from django.contrib import admin
from .models import Category, Product
import uuid

# Register your models here.


@admin.action(description="Regenerate SKU")
def regenerate_sku(modeladmin, request, queryset):
    queryset.update(sku=uuid.uuid4())


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'size',
        'unit',
        'price',
        'rating',
        'has_strength',
        'strength',
        'image',
        'sku',
    )
    readonly_fields = ["sku"]
    actions = [regenerate_sku]
    # exclude = ["sku"]

    # ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
