from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
from decimal import Decimal


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Category(BaseModel):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "categories"


class Product(BaseModel):
    class RatingChoice(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    discount = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    rating = models.PositiveIntegerField(choices=RatingChoice.choices, default=RatingChoice.ONE.value)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def discounted_price(self):
        if self.discount > 0:
            self.price = self.price * Decimal(1 - self.discount / 100)
        return Decimal(f'{self.price}').quantize(Decimal('0.00'))

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=400)
    content = models.TextField(null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} | {self.email}"


class Order(models.Model):
    phone_validator = RegexValidator(
        regex=r'^\+998\d{9}$',
        message="Telefon raqami +998 bilan boshlanib, 9 ta belgidan iborat bo‘lishi kerak."
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, validators=[phone_validator])
    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} | {self.product} | {self.quantity}"