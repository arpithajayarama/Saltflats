from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class UserProfile(models.Model):
  user = models.OneToOneField(User)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  title= models.CharField(max_length=30)
  subject_major= models.CharField(max_length=30)
  address = models.CharField(max_length=50)
  city = models.CharField(max_length=60)
  state_province = models.CharField(max_length=30)
  country = models.CharField(max_length=50)
  email = models.EmailField()
  phone=models.CharField(max_length=50)
  hr_rate = models.DecimalField(max_digits=16, decimal_places=2,blank=True ,null=True)
  maxhrs_week=models.DecimalField(max_digits=16, decimal_places=2,blank=True ,null=True)
  image =models.ImageField(upload_to='profile_image',blank=True)

  def __str__(self):
   return self.user.username



def Create_Profile(sender, **kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(Create_Profile, sender=User,)
