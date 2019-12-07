from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(MarketOrder)
admin.site.register(Bid)
admin.site.register(ExecutedOrder)
admin.site.register(FuturesContract)
admin.site.register(FutureBid)
admin.site.register(FutureDeal)
admin.site.register(CityCrop)
admin.site.register(CropProduction)

