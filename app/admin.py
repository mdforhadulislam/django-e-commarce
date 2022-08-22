from django.contrib import admin

from .models import (Accessories, Bagpack, Catagory, Jewellery, Mans,
                     ProducatStatus, UserProfile, Womans,Producat)

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
