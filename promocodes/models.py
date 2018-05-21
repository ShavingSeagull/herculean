from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class PromoCode(models.Model):
    name = models.CharField(max_length=40, null=False)
    code = models.CharField(max_length=10, unique=True)
    start_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()

    def __str__(self):
        return self.name
