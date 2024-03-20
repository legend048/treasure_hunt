from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from .models import event, qr
from treasure_hunt.settings import BASE_DIR
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
    cont = {
        'event_code': list(event.objects.filter(event_id=ev_id).values())[0]['event_code'],
        'qr': list(qr.objects.filter(event_id = ev_id).values())
    }
    # print(event.objects.filter(event_id=ev_id).values_list())
    # cont = [x['image'].replace('media', 'static') for x in cont]
    print(cont)
    return render(request, 'setup/details.html', {'context' : cont})

