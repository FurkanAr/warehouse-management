from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ('Book', 'Book'),
    ('Self-Care', 'Self-Care'),
    ('Electronics', 'Electronics'),
    ('Fashion', 'Fashion'),
    ('Food', 'Food'),
    ('Toy', 'Toy'),
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name 
    
    class Meta:
        ordering = ('name',)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name