from django.contrib import admin

from .models import Product, Order, CustomJersey


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "price",
        "size",
        "stock",
        "is_featured",
        "created_at",
    )

    list_filter = (
        "category",
        "is_featured",
    )

    search_fields = (
        "name",
        "description",
    )

    list_editable = (
        "price",
        "stock",
        "is_featured",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "customer_name",
        "phone",
        "product",
        "quantity",
        "size",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "customer_name",
        "phone",
        "product__name",
    )

    list_editable = (
        "status",
    )


@admin.register(CustomJersey)
class CustomJerseyAdmin(admin.ModelAdmin):

    list_display = (
        "customer_name",
        "phone",
        "team",
        "name_on_jersey",
        "number",
        "size",
        "status",
    )

    list_filter = (
        "status",
        "size",
    )

    search_fields = (
        "customer_name",
        "phone",
        "team",
        "name_on_jersey",
    )

    list_editable = (
        "status",
    )