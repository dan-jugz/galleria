from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image

# Create your views here.
def home(request):
    return HttpResponse(request,'home.html')

def images_of_day(request):
    date =dt.date.today()
    images=Article.todays_images()

    return render(request, 'all-images/today-images.html',{"date":date,'images':images})

