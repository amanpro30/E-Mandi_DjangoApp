from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# from order.models import ExecutedOrder
from django.dispatch import *
from django.db.models.signals import post_save



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length =100, default='')
    phone = models.BigIntegerField(default=0)
    image = models.ImageField(upload_to='image_profile', blank=True)
    state = models.CharField(max_length =100, default='')
    city = models.CharField(max_length =100, default='')
    street = models.CharField(max_length =500, default='')
    aadharcard = models.BigIntegerField( default=0)
    pincode = models.IntegerField(default=0)
    email_confirmed = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.user.username}'


# class ReviewdUser(models.Model):
#     user=models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username

class UserReview(models.Model):
    user = models.ForeignKey(UserProfile, null=True, related_name='userreviewing',on_delete=models.CASCADE)
    revieweduser = models.ForeignKey(UserProfile, null=True, related_name='revieweduser',on_delete=models.CASCADE)
    rating=models.FloatField(default=0.0)
    review=models.CharField(max_length =500, default='')

    def __str__(self):
        return str(self.revieweduser.user)

class AvgRating(models.Model):
    user=models.ForeignKey(UserProfile,null=True,on_delete=models.CASCADE)
    avgrating=models.FloatField(default=0.0)
    def __str__(self):
        return str(self.user)

def updateAvg(sender, **kwargs):
    if kwargs['created']:
        print(kwargs['instance'].__dict__)
        print(kwargs['instance'].revieweduser)
        rating_instances = UserReview.objects.filter(revieweduser=kwargs['instance'].revieweduser)
        cnt_rating = rating_instances.count()
        try:
            avgrating = AvgRating.objects.get(user=kwargs['instance'].revieweduser).avgrating
        except:
            avgrating = 0

        new_avg_rating = (avgrating * (cnt_rating-1) + kwargs['instance'].rating) / cnt_rating
        AvgRating.objects.filter(user=kwargs['instance'].revieweduser).delete()
        AvgRating.objects.create(user=kwargs['instance'].revieweduser,avgrating=new_avg_rating)

  
# class OrderReview(models.Model):
#     order=models.ForeignKey(ExecutedOrder, on_delete=models.CASCADE)
#     rating=models.FloatField(default=0.0)
#     review=models.CharField(max_length =500, default='')

#     def __str__(self):
#         return f'{self.order.orderid.CropName}{self.order.buyerid.username} OrderReview'

post_save.connect(updateAvg, sender=UserReview)
