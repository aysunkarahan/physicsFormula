import random
from django.http import HttpResponse
##from django.template import loader

from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Seviye, Kelime
#def (request):
    ######all_albums = Album.objects.all()
    #####html =''
    ####for album in all_albums:
    ###    url = '/music/'+ str(album.id) + '/'
    ##    html += '<a href="'+ url +'">'+ album.album_title +'</a><br>'
    #return HttpResponse(html)#

def index(request):
    seviyeler = Seviye.objects.all()
    #template = loader.get_template('music/index.html')
    #context = {'all_albums' : all_albums,}
    #return HttpResponse(template.render(context, request))
    return render(request, 'Formula/index.html', {'seviyeler' : seviyeler})



def detail(request, seviye_id):
    try:
        seviye = get_object_or_404(Seviye, pk=seviye_id)
        meviye = seviye.kelime_set.all
        n = random.randrange(1,25) # returns a random integer
        random_kelime = random.randrange(1, 25) # returns a random integer
    except Seviye.DoesNotExist:
        raise Http404("Album bulunamadı")

    return render(request, 'Formula/detail.html', {'meviye': meviye, 'random_kelime': random_kelime, 'n': n})
    #return HttpResponse("<h2>Album detayı id :"+str(album_id) +"</h2>")
