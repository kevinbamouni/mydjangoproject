from django.shortcuts import render
from .models import Artists
from .models import Albums

# Create your views here.
def index(request):
    return render(request, 'chinook/index.html')

def chinookdataview(request):
    latest_question_list = Artists.objects.all()
    context = {'Artists': latest_question_list}
    return render(request, 'chinook/data.html', context)

def chinookalbumview(request):
    Albums_list = Albums.objects.all()
    context = {'Albums': Albums_list}
    return render(request, 'chinook/albums.html', context)