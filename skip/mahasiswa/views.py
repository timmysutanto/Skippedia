from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Mahasiswa, Komentar, Rating

# Create your views here.
def index(request):
    mahasiswa_list = Mahasiswa.objects.all()
    context = { 'mahasiswa_list': mahasiswa_list }
    return render(request, 'mahasiswa/index.html', context)

def profil(request, nim):
    m = Mahasiswa.objects.get(pk=nim)
    return render(request, 'mahasiswa/profil.html', {'mahasiswa': m})

def rate(request, nim):
    m = Mahasiswa.objects.get(pk=nim)
    if request.method != 'POST':
        return render(request, 'mahasiswa/rate.html', {'mahasiswa' : m} )
    else:
        m.rating_set.create(rate=request.POST['rate'])
    # return render(request, 'mahasiswa/rate.html', {'mahasiswa' : m} )
    # m.rating_set.create(rate=request.POST.get('rate', 1))
    # # render(request, 'mahasiswa/rate.html', {'mahasiswa' : m})  
    # # r += 1
    # r.save()
        # return HttpResponse('tes')
        return HttpResponseRedirect(reverse('mahasiswa:profil', args=(m.nim, )))

def comment(request, nim):
    m = Mahasiswa.objects.get(pk=nim)
    if request.method != 'POST':
        return render(request, 'mahasiswa/comment.html', {'mahasiswa' : m})
    else:
        m.komentar_set.create(isi_komentar=request.POST['comment'])
        return HttpResponseRedirect(reverse('mahasiswa:profil', args=(m.nim, )))
        