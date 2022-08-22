from app.models import Producat, ProducatStatus
from django.conf import settings
from django.shortcuts import render


def home(request):
   Producat_all_data = Producat.objects.all()
   new_all_Producat_data = Producat.objects.filter(status=2)
   popular_all_Producat_data = Producat.objects.filter(status=3)

   data = {
      "all_producat_data":Producat_all_data,
      "new_all_Producat_data":new_all_Producat_data,
      "popular_all_Producat_data":popular_all_Producat_data
   }

   return render(request,'home.html',data)

def about(request):
   return render(request,'aboutus.html')

def shop(request):
   all_Producat_data = Producat.objects.all()
   print(all_Producat_data)
   data={
      "all_Producat_data":all_Producat_data,
      "MEDIA_URL":settings.MEDIA_URL,
      "MEDIA_ROOT":settings.MEDIA_ROOT
   }
   return render(request,'shops.html',data)

def contact(request):
   return render(request,'contact.html')


def single_producat(request,producat_id):
   Producat_data = Producat.objects.get(id=producat_id)
   all_Producat_data = Producat.objects.all()
   data = {
     "Producat_data":Producat_data,
     "all_Producat_data":all_Producat_data,
     "MEDIA_URL":settings.MEDIA_URL,
     "MEDIA_ROOT":settings.MEDIA_ROOT
   }
   return render(request,'single-producat.html',data)
