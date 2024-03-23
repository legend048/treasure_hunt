from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from .models import event, qr, player, scanned_qr
from django.contrib.auth.decorators import login_required
from treasure_hunt.settings import BASE_DIR
from django.utils import timezone
from django.shortcuts import render
from django.db.models import Count

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

@login_required
def join(request):
    if request.method == 'POST':
        game_id = request.POST['game_id']
        try:
            joined_event = event.objects.get(event_code=game_id)
            # Check if user already joined
            if not player.objects.filter(event=joined_event, player=request.user).exists():
                new_player = player.objects.create(event=joined_event, player=request.user)
                new_player.save()
                message = f"Welcome, {request.user.username}! You've successfully joined the game: {joined_event.event_code}"
            else:
                message = f"You're already in the game: {joined_event.event_code} user: {request.user}. Ready to scan some QRs?"
        except event.DoesNotExist:
            message = "Invalid Game ID. Please try again."
        return render(request, 'setup/join_game.html', {'message': message})
    else:
        return render(request, 'setup/join_game.html')

# def scan_qr(request):
#     print(*request)
#     if request.method == 'POST':
#         # Implement logic to process scanned QR code data (e.g., using ZXing or ZBar libraries)
#         qr_code = request.POST['qr_code']  # Replace with actual QR data extraction
#         print(qr_code)
#         print(request.user)
#         try:
#             # Retrieve the QR object based on the scanned code (replace with actual logic)
#             scanned_qr = qr.objects.get(qr_id=qr_code)  # Replace with appropriate field/logic
#             if scanned_qr.event.event_active:  # Check if the event is active
#                 if request.user not in scanned_qr.scanned_by.all():  # Check if user hasn't scanned yet
#                     scanned_qr.scanned_by.add(request.user)  # Add user to scanned_by using ManyToManyField
#                     scanned_qr.scanned_at = timezone.now()  # Update scanned_at
#                     scanned_qr.save()
#                     message = "QR Scanned Successfully!"
#                 else:
#                     message = "You have already scanned this QR."
#             else:
#                 message = "This game is not currently active."
#         except qr.DoesNotExist:
#             message = "Invalid QR Code."
#         return render(request, 'setup/scan_qr.html', {'message': message})
#     else:
#         return render(request, 'setup/scan_qr.html')

@login_required
def scan_qr(request):
    print(*request)
    if request.method == 'POST':
        qr_code = request.POST['qr_code']
        try:
            scanned_qr_obj = qr.objects.get(qr_id=qr_code)
            print(f'scanned obj - {scanned_qr_obj}')
            if scanned_qr_obj.event.event_active:
                scanned_already = scanned_qr.objects.filter(qr_id=scanned_qr_obj, scanned_by=request.user).exists()
                if not scanned_already:
                    scanned_qr.objects.create(qr_id=scanned_qr_obj, scanned_by=request.user, email=request.user.email, scanned_at=timezone.now())
                    message = "QR Scanned Successfully!"
                else:
                    message = "You have already scanned this QR."
            else:
                message = "This game is not currently active."
        except qr.DoesNotExist:
            message = "Invalid QR Code."
        return render(request, 'setup/scan_qr.html', {'message': message})
    else:
        return render(request, 'setup/scan_qr.html')


    
# def leaderboard_view(request):
#     events = event.objects.all()
#     leaderboard_data = []
#     for event in events:
#         player_scans = event.player_set.annotate(scan_count=Count('scanned_by')).order_by('-scan_count')
#         for player in player_scans:
#             leaderboard_data.append({
#                 'event_id': event.id,
#                 'event_code': event.event_code,
#                 'player_username': player.player.username,
#                 'scan_count': player.scan_count
#             })

#     return render(request, 'leaderboard.html', {'leaderboard_data': leaderboard_data})

