from django.contrib import admin
from .models import Product, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    max_num = 1

    def get_extra(self, request, obj=None, **kwargs):
        """Dynamically sets the number of extra forms. 0 if the related object
        already exists or the extra configuration otherwise."""
        if obj:
            # Don't add any extra forms if the related object already exists.
            return 0
        return self.extra

class ProductsAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

    fields = ('name', 'description', 'price', 'choice', 'sku')

admin.site.register(Product, ProductsAdmin)
