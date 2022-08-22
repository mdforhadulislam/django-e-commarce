from django.contrib.auth.models import User
from django.db import models

# Create your models here.
DEFAULT = 'default.jpg'


class UserProfile(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)


class Catagory(models.Model):
   title = models.CharField(max_length=50,null=True)
   id= range(1,1000000)
   def __str__(self):
      return self.title


class ProducatStatus(models.Model):
   title = models.CharField(max_length=50,null=True)
   id = range(1,1000000)
   def __str__(self):
      return self.title
      

class Producat(models.Model):
   title = models.CharField(max_length=50,null=True)
   price = models.IntegerField(null=True)
   deprition = models.TextField()
   status = models.ForeignKey(ProducatStatus,on_delete=models.CASCADE)
   producat_catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)
   produca_image_1 = models.ImageField(upload_to='producats',default=DEFAULT)
   produca_image_2 = models.ImageField(upload_to='producats',default=DEFAULT)
   produca_image_3 = models.ImageField(upload_to='producats',default=DEFAULT)
   produca_image_4 = models.ImageField(upload_to='producats',default=DEFAULT)
   produca_image_5 = models.ImageField(upload_to='producats',default=DEFAULT)
   is_stock = models.BooleanField(default=True)
   is_discount = models.IntegerField(default=00)
   # collor =  models.ForeignKey(ProducatCollor,on_delete=models.CASCADE)

   def __str__(self):
      return self.title


class Mans(models.Model):
   title = "Mans"
   collection_year = models.CharField(max_length=5,null=True)
   produca_image = models.ImageField(upload_to='producats')
   id= range(1,1000000)
   def __str__(self):
      return f'{self.id}-{self.title}-{self.collection_year}'


class Womans(models.Model):
   title = "Womans"
   collection_year = models.CharField(max_length=5,null=True)
   produca_image = models.ImageField(upload_to='producats')
   id= range(1,1000000)
   def __str__(self):
      return f'{self.id}-{self.title}-{self.collection_year}'


class Jewellery(models.Model):
   title = "Jewellery"
   collection_year = models.CharField(max_length=5,null=True)
   produca_image = models.ImageField(upload_to='producats')
   id= range(1,1000000)
   def __str__(self):
      return f'{self.id}-{self.title}-{self.collection_year}'


class Bagpack(models.Model):
   title = "Bagpack"
   collection_year = models.CharField(max_length=5,null=True)
   produca_image = models.ImageField(upload_to='producats')
   id= range(1,1000000)
   def __str__(self):
      return f'{self.id}-{self.title}-{self.collection_year}'



class Accessories(models.Model):
   title = "Accessories"
   collection_year = models.CharField(max_length=5,null=True)
   produca_image = models.ImageField(upload_to='producats')
   id= range(1,1000000)
   def __str__(self):
      return f'{self.id}-{self.title}-{self.collection_year}'

