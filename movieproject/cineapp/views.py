from django.http import HttpResponse
from django.shortcuts import render, redirect
from. models import movie
from. forms import movieform
# Create your views here.
def demo(request):
    cinema=movie.objects.all()
    context={
        'movie_list':cinema
    }
    return render(request,"index.html",context)

def detail (request,movie_id):
    obj=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':obj})

def add_movie(request):
    if request.method=="POST":
        name =  request.POST.get('name',)
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        project=movie(name=name,desc=desc,year=year,img=img)
        project.save()

    return render(request,'add.html')

def update(request,movie_id):
    j = movie.objects.get(id=movie_id)
    k = movieform(request.POST or None,request.FILES,instance=j)
    if k.is_valid():
        k.save()
        return redirect('/')
    return render(request,'edit.html',{'form':k,'movie':j})

def delete(request,id):
    if request.method=='POST':
        mov=movie.objects.get(id=id)
        mov.delete()
        return redirect('/')
    return render(request,'delete.html')