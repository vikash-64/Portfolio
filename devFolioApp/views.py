from django.shortcuts import render , HttpResponse
from . models import Project , StaticThings 


# Create your views here.




def index(request):
    blog = Project.objects.all()
    context = {'blogs' : blog}
    mything = StaticThings.objects.all()
    context = {'myt' : mything}
    
    return render(request, 'index.html' , context)
