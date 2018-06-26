from django.db import models
from products.models import Product


class Order(models.Model):
    COUNTRIES = (
        ('albania', 'Albania'),
        ('algeria', 'Algeria'),
        ('andorra', 'Andorra'),
        ('argentina', 'Argentina'),
        ('armenia', 'Armenia'),
        ('australia', 'Australia'),
        ('austria', 'Austria'),
        ('azerbaijan', 'Azerbaijan'),
        ('belarus', 'Belarus'),
        ('belgium', 'Belgium'),
        ('bermuda', 'Bermuda'),
        ('bosnia', 'Bosnia'),
        ('brazil', 'Brazil'),
        ('bulgaria', 'Bulgaria'),
        ('canada', 'Canada'),
        ('chile', 'Chile'),
        ('china', 'China'),
        ('colombia', 'Colombia'),
        ('costa_rica', 'Costa Rica'),
        ('croatia', 'Croatia'),
        ('cyprus', 'Cyprus'),
        ('czech_republic', 'Czech Republic'),
        ('denmark', 'Denmark'),
        ('ecuador', 'Ecuador'),
        ('egypt', 'Egypt'),
        ('estonia', 'Estonia'),
        ('finland', 'Finland'),
        ('france', 'France'),
        ('georgia', 'Georgia'),
        ('germany', 'Germany'),
        ('greece', 'Greece'),
        ('guatemala', 'Guatemala'),
        ('honduras', 'Honduras'),
        ('hungary', 'Hungary'),
        ('iceland', 'Iceland'),
        ('india', 'India'),
        ('indonesia', 'Indonesia'),
        ('israel', 'Israel'),
        ('italy', 'Italy'),
        ('jamaica', 'Jamaica'),
        ('japan', 'Japan'),
        ('latvia', 'Latvia'),
        ('liechtenstein', 'Liechtenstein'),
        ('lithuania', 'Lithuania'),
        ('luxembourg', 'Luxembourg'),
        ('macedonia', 'Macedonia'),
        ('malaysia', 'Malaysia'),
        ('maldives', 'Maldives'),
        ('malta', 'Malta'),
        ('mexico', 'Mexico'),
        ('moldova', 'Moldova'),
        ('monaco', 'Monaco'),
        ('montenegro', 'Montenegro'),
        ('morocco', 'Morocco'),
        ('netherlands', 'Netherlands'),
        ('new_zealand', 'New Zealand'),
        ('norway', 'Norway'),
        ('peru', 'Peru'),
        ('philippines', 'Philippines'),
        ('poland', 'Poland'),
        ('portugal', 'Portugal'),
        ('south_korea', 'Republic of Korea'),
        ('romania', 'Romania'),
        ('russia', 'Russia'),
        ('serbia', 'Serbia'),
        ('singapore', 'Singapore'),
        ('slovakia', 'Slovakia'),
        ('slovenia', 'Slovenia'),
        ('south_africa', 'South Africa'),
        ('spain', 'Spain'),
        ('sweden', 'Sweden'),
        ('switzerland', 'Switzerland'),
        ('thailand', 'Thailand'),
        ('tunisia', 'Tunisia'),
        ('turkey', 'Turkey'),
        ('ukraine', 'Ukraine'),
        ('uae', 'United Arab Emirates'),
        ('uk', 'United Kingdom'),
        ('usa', 'United States'),
    )

    full_name = models.CharField(max_length=50, blank=False)
    house_number = models.CharField(max_length=20, blank=False, verbose_name='House number/name')
    address1 = models.CharField(max_length=40, blank=False, verbose_name='Street')
    address2 = models.CharField(max_length=40, blank=True, verbose_name='Address Line 2 (optional)')
    city = models.CharField(max_length=40, blank=False, verbose_name='Town/City')
    county = models.CharField(max_length=40, blank=False, verbose_name='County/State/Province')
    post_code = models.CharField(max_length=20, blank=False, verbose_name='Postal/Zip Code')
    country = models.CharField(max_length=20, blank=False, choices=COUNTRIES)
    phone_number = models.CharField(max_length=20, blank=False, verbose_name='Phone Number (needed for delivery)')
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product,on_delete=models.CASCADE , null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} {2}".format(self.quantity, self.product.name, self.product.product_sku)
