from django.db import models
from products.models import Product
from accounts.models import Profile

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.BooleanField(verbose_name="Do you recommend this product? (Click if you do!)")
    created_date = models.DateTimeField(auto_now_add=True)