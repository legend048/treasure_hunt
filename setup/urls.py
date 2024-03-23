from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.setup, name='setup'),
    # path('qr', views.details, name = 'details')
    path('qr/<slug:ev_id>', views.details, name ='details'),
    path('join', views.join, name='join'),
    path('scan_qr', views.scan_qr, name='scan_qr'),
]