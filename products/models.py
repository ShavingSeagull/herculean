from django.db import models
from django.template.defaultfilters import slugify
import os


class Product(models.Model):
    CHOICES = (
        ('accessories', 'Accessories'),
        ('amino_acids', 'Amino-Acids'),
        ('creatine', 'Creatine'),
        ('equipment', 'Equipment'),
        ('protein', 'Protein'),
        ('supplements', 'Supplements')
    )

    name = models.CharField(max_length=30, default='')
    slug = models.SlugField(max_length=70, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    choice = models.CharField(max_length=11, choices=CHOICES)

    def __str__(self):
        return self.name

    # Custom save method to set the slug. Sets slug once on object creation to avoid broken links if title is changed
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(Product, self).save(*args, **kwargs)


def upload_image(instance, filename):
    choice = instance.product.choice

    if choice == 'accessories':
        return os.path.join('img/products/accessories', filename)
    elif choice == 'amino_acids':
        return os.path.join('img/products/amino_acids', filename)
    elif choice == 'creatine':
        return os.path.join('img/products/creatine', filename)
    elif choice == 'equipment':
        return os.path.join('img/products/equipment', filename)
    elif choice == 'protein':
        return os.path.join('img/products/protein', filename)
    elif choice == 'supplements':
        return os.path.join('img/products/supplements', filename)


class Image(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image)
