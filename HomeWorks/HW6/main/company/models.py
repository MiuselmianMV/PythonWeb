from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Seller(models.Model):

    class Position(models.TextChoices):
        SELLER = 'seller', 'Продавец'
        SENIOR = 'senior_seller', 'Старший продавец'
        HEAD = 'head_of_sales', 'Руководитель отдела продаж'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    hired_date = models.DateField()
    position = models.CharField(
        max_length=20,
        choices=Position.choices,
        default=Position.SELLER
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_position_display()})" #type: ignore



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity_in_stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Sale #{self.id} — {self.product.name}" #type: ignore
