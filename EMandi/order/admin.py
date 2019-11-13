from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(MarketOrder)
admin.site.register(Bid)
admin.site.register(ExecutedOrder)
