from datetime import date

from django.db import models
from django.utils.timezone import now


# Create your models here.
class Product(models.Model):
    p_name = models.CharField(max_length=50)
    creator = models.ForeignKey("auth.User")
    category = models.CharField(max_length=100)
    main_image = models.ImageField(upload_to="Products/", null=True)
    screenshot2 = models.ImageField(upload_to="products/", null=True,)
    screenshot3 = models.ImageField(upload_to="products/", null=True)
    created = models.DateField(default=now,null=True)
    updated = models.DateField(default=now,null=True)
    actual_price = models.IntegerField(default=2000)
    quantity = models.IntegerField(default=5)
    product_file = models.FileField(upload_to="doc_files", null=False)

    def publish(self):
        self.save()

    def __str__(self):
        return self.p_name


class Giveaway(models.Model):
    g_name = models.CharField(max_length=55,blank=False, null=False)
    user = models.ForeignKey("auth.User")
    p_name = models.ForeignKey("Product")
    entries = models.IntegerField(default=5)
    created = models.DateField(default=now)
    updated = models.DateField(default=now)
    image = models.ImageField(upload_to="giveaways/Img/", null=True)
    description = models.TextField( blank=False, null=False)
    price = models.IntegerField(default=2000)
    ending_time = models.DateField(default=now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.g_name


class GiveawayEntry(models.Model):
    user= models.PositiveIntegerField("auth.User")
    giveaway = models.PositiveIntegerField("Giveaway")
    created_on = models.DateField(default=now)
    updated = models.DateField(default=now)
    total_points = models.IntegerField()
    facebook_share_count = models.IntegerField(default=0)
    twitter_share_count = models.IntegerField(default=0)
    google_plus_share_count = models.IntegerField(default=0)
    stumble_share_count = models.IntegerField(default=0)
    linked_share_count = models.IntegerField(default=0)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.id)
