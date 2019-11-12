from django.contrib import admin

from .models import *

admin.site.register(Transaction)
admin.site.register(BankDetails)
admin.site.register(Balance)