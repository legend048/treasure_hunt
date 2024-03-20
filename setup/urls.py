from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.setup, name='setup'),
    # path('qr', views.details, name = 'details')
    path('qr/<slug:ev_id>', views.details, name ='details')
] 