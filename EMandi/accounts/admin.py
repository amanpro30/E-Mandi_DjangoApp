from django.contrib import admin

from .models import *

admin.site.register(UserProfile)
admin.site.register(UserReview)
# admin.site.register(ReviewdUser)
admin.site.register(AvgRating)
