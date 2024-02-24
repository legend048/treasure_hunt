from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from .models import event 
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the setup index.")
def setup(request):
    if request.method == 'POST':
        form = forms.eventForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            # Set event_active manually
            form.event_active = True  # or False, depending on your logic
            form.event_organizer = request.user
            # ev = event.objects.get()
            form.save()
            event_obj = event.objects.get(event_organizer = request.user).first()
            ev_id = event_obj.objects.get('event_id')
            # return HttpResponse("Event Created")
        return redirect('qr', ev_id = ev_id )
    else:       
        form = forms.eventForm()
        return render(request, "setup/setup.html",{'form':form})
    # return HTTPResponse("Hello, world. You're at the setup index.")
def details(request, ev_id):
    return render(request, 'setup/qr.html', {ev_id : ev_id})
