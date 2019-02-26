from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Events,Attendees

def index(request):
    context = {
        "events": Events.objects.all()
    }
    return render(request,"myapp/index.html",context)
    

def add(request):
    if request.method=="POST":
        
        
        Attendees(first_name=request.POST["fname"],last_name=request.POST["lname"],events=request.POST["event_sel"]).save()

    return HttpResponseRedirect(reverse("index"))