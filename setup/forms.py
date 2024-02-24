from django import forms
from .models import event,qr
# class eventForm(forms.Form):
#     start = forms.DateTimeField()
#     end = forms.DateTimeField()
#     number_of_qr = forms.IntegerField()

# class qrForm(forms.Form):
    # template = forms.ImageField()

class eventForm(forms.ModelForm):
    class Meta:
        model = event
        fields = ['number_of_qr','start','end']

class qrForm(forms.ModelForm):
    class Meta:
        model = qr
        fields = ['image', 'hint']
