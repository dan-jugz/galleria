from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image

# Create your views here.
def home(request):
    return HttpResponse(request,'home.html')

def images_of_day(request):
    date =dt.date.today()
    images=Image.todays_images()

    return render(request, 'all-images/today-images.html',{"date":date,'images':images})

#presents news from past days
def past_days_images(request,past_date):

    try:
    #converts data from the string url
        date = dt.datetime.strptime(past_date,'%y-%m-%d').date()

    except ValueError:
        #raise 404 error when valueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(images_today)
    images = image.days_images(date)

    return render(request, 'all-images/past-images.html',{"date": date,"images":images})