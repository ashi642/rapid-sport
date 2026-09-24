from django.db import models


class Product(models.Model):

    CATEGORY_CHOICES = [
        ("Football", "Football"),
        ("Cricket", "Cricket"),
        ("Custom", "Custom"),
        ("Accessories", "Accessories"),
    ]

    name = models.CharField(max_length=200)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    size = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: S, M, L, XL, XXL"
    )

    stock = models.PositiveIntegerField(default=0)

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    description = models.TextField(blank=True)

    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]


class Order(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
    ]

    customer_name = models.CharField(max_length=150)

    phone = models.CharField(max_length=20)

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    size = models.CharField(max_length=50)

    quantity = models.PositiveIntegerField(default=1)

    custom_name = models.CharField(
        max_length=100,
        blank=True
    )

    custom_number = models.CharField(
        max_length=20,
        blank=True
    )

    address = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.product.name}"

    @property
    def total_price(self):
        return self.product.price * self.quantity

    class Meta:
        ordering = ["-created_at"]


class CustomJersey(models.Model):

    SIZE_CHOICES = [
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
        ("XXL", "XXL"),
    ]

    customer_name = models.CharField(max_length=150)

    phone = models.CharField(max_length=20)

    name_on_jersey = models.CharField(max_length=100)

    number = models.PositiveIntegerField()

    team = models.CharField(max_length=150)

    size = models.CharField(
        max_length=10,
        choices=SIZE_CHOICES
    )

    logo = models.ImageField(
        upload_to="logos/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=[
            ("Pending", "Pending"),
            ("Approved", "Approved"),
            ("Completed", "Completed"),
        ],
        default="Pending"
    )

    def __str__(self):
        return f"{self.customer_name} - {self.team}"