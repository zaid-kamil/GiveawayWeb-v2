from django.contrib import admin

# Register your models here.
from products.models import Product
from products.models import Giveaway
from products.models import GiveawayEntry

admin.site.register(Product)
admin.site.register(Giveaway)
admin.site.register(GiveawayEntry)
