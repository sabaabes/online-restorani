from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="კატეგორიის სახელი")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="კერძის სახელი")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="ფასი")
    description = models.TextField(blank=True, null=True, verbose_name="აღწერა")
    image = models.URLField(blank=True, null=True, verbose_name="სურათის ლინკი")
    is_available = models.BooleanField(default=True, verbose_name="მარაგშია")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="კატეგორია")

    def __str__(self):
        return self.name