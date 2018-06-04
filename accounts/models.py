from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
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
        ('romania', 'Romania'),
        ('russia', 'Russia'),
        ('serbia', 'Serbia'),
        ('singapore', 'Singapore'),
        ('slovakia', 'Slovakia'),
        ('slovenia', 'Slovenia'),
        ('south_africa', 'South Africa'),
        ('south_korea', 'Republic of Korea'),
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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, default="This user likes to keep an air of mystery about them.")
    location = models.CharField(max_length=30, blank=True, default="???")
    profile_pic = models.ImageField(upload_to="img/profiles", blank=True, null=True)
    house_number = models.CharField(max_length=20, verbose_name='House number/name *')
    address1 = models.CharField(max_length=60, verbose_name='Street *')
    address2 = models.CharField(max_length=60, blank=True, verbose_name='Secondary address line')
    city = models.CharField(max_length=20, verbose_name='Town/City *')
    county = models.CharField(max_length=30, verbose_name='County/State/Province *')
    post_code = models.CharField(max_length=10, verbose_name='Post/Zip Code *')
    country = models.CharField(max_length=20, choices=COUNTRIES, null=True, verbose_name='Country *')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
