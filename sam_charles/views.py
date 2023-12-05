from django.shortcuts import render, HttpResponse

from .models import Song

# Create your views here.
def index(request):
    songs = Song.objects.all()
    context = {
        'songs': songs,
    }
    
    return render(request, 'sam_charles/index.html', context)