from django.contrib import admin

from .models import (Accessories, Bagpack, Catagory, Jewellery, Mans,
                     ProducatStatus, UserProfile, Womans,Producat,ProducatSize,ProducatCollor)

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Catagory)
admin.site.register(ProducatStatus)
admin.site.register(Mans)
admin.site.register(Womans)
admin.site.register(Jewellery)
admin.site.register(Bagpack)
admin.site.register(Accessories)
admin.site.register(Producat)
admin.site.register(ProducatSize)
admin.site.register(ProducatCollor)
