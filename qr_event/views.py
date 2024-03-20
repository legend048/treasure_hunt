from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the setup index.")

def join(request):
    if request.method == 'POST':
        event_code = request.POST.get('event_code')
        return redirect('home', event_code = event_code)
    else:
        return render(request, 'qr_event/join.html')

def home(request, event_code):
    
    return render(request, 'qr_event/home.html')