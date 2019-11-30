# this file contains all file used for visitor app

from django import forms
from .models import Visitor
from host.models import Host

HOST = [(host['id'], Host.objects.filter(id=host['id']).first().user.first_name) for host in Host.objects.values()]


# Visitor entry form
class EntryForm(forms.Form):
    First_name = forms.CharField(max_length=100)
    Last_name = forms.CharField(max_length=100)
    Phone_number = forms.CharField(max_length=10)
    Email = forms.EmailField()
    Address_visited = forms.CharField(widget=forms.Textarea)
    host_name = forms.ChoiceField(choices=HOST)


# Checkout confirm form
class CheckoutConfirmForm(forms.Form):
    CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )
    Do_You_Want_To_Check_Out = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)


# Checkout form
class CheckoutForm(forms.Form):
    first_Name = forms.CharField(max_length=100)
    phone_Number = forms.CharField(max_length=10)
