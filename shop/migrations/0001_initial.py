# Generated by Django 5.1.7 on 2025-03-12 23:11

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("my_order", models.PositiveIntegerField(default=0)),
                ("title", models.CharField(max_length=255, unique=True)),
            ],
            options={
                "verbose_name_plural": "categories",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("my_order", models.PositiveIntegerField(default=0)),
                ("name", models.CharField(max_length=255, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=14)),
                ("image", models.ImageField(upload_to="images/")),
                ("discount", models.PositiveIntegerField(default=0)),
                (
                    "rating",
                    models.PositiveIntegerField(
                        choices=[
                            (1, "One"),
                            (2, "Two"),
                            (3, "Three"),
                            (4, "Four"),
                            (5, "Five"),
                        ],
                        default=1,
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="shop.category",
                    ),
                ),
            ],
            options={
                "ordering": ["my_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "phone",
                    models.CharField(
                        max_length=20,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="The phone number must start with +998 and consist of 9 characters.",
                                regex="^\\+998\\d{9}$",
                            )
                        ],
                    ),
                ),
                (
                    "quantity",
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(4),
                        ]
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=400)),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="shop.product",
                    ),
                ),
            ],
        ),
    ]
