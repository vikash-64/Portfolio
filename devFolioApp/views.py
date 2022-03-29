from django.shortcuts import render , HttpResponse
from . models import Project 


# Create your views here.




def index(request):
    blog = Project.objects.all()
    context = {'blogs' : blog}
    
    return render(request, 'index.html' , context)
