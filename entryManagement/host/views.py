from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Host
from visitor.models import Visitor
from django.core.paginator import Paginator


def Home(request):
    context = {
        'title': "Host Dashboard",
    }
    return render(request, 'host/home.html', context)

def HostRegister(request):
    if request.method == 'GET':
        UserRegisterForm = forms.UserRegisterForm()
        HostRegisterForm = forms.HostRegisterForm()
        context = {
            'title': 'Register Host',
            'form1' : HostRegisterForm,
            'form2': UserRegisterForm,
        }
        return render(request, 'host/register.html', context)
    else:
        UserRegisterForm = forms.UserRegisterForm(request.POST)
        HostRegisterForm = forms.HostRegisterForm(request.POST)
        if UserRegisterForm.is_valid() and HostRegisterForm.is_valid():
            newUser = UserRegisterForm.save()
            newHost_phone = HostRegisterForm.cleaned_data['phone_Number']
            newHost = Host.objects.create(
                user=newUser,
                phone_Number=newHost_phone,
            )
            newHost.save()
        return redirect("hostHome")


# Handles route '/past-meetings/'
# Shows all past meetings
def pastMeetings(request):
    pastVisitors = Visitor.objects.filter(is_checked_in='No').\
        order_by('-checkoutTime')
    pastVisitorsList = []
    for visitor in pastVisitors:
        pastVisitorsList.append(
            {
                'first_name': visitor.first_name,
                'last_name': visitor.last_name,
                'visitor_phone': visitor.phone_Number,
                'checkInTime': visitor.checkInTime,
                'checkoutTime': visitor.checkoutTime,
                'host': visitor.host.user.first_name,
                'host_phone': visitor.host.phone_Number,
            }
        )
    # Paginator shows limited number of visitors
    paginator = Paginator(pastVisitorsList, 6)
    page = request.GET.get('page')
    past_VisitorsList = paginator.get_page(page)

    context = {
        'title': "Past Meetings",
        'visitors': past_VisitorsList,
    }
    return render(request, 'host/previousMeetings.html', context)


# Handles route '/running-meetings/'
# Shows all currently running meetings
def runningMeetings(request):
    currentVisitors = Visitor.objects.filter(is_checked_in='Yes').\
        order_by('-checkInTime')
    runningMeetings = []
    for entry in currentVisitors:
        runningMeetings.append(
            {
                'firstName': entry.first_name,
                'lastName': entry.last_name,
                'visitor_phone': entry.phone_Number,
                'host': entry.host.user.first_name,
                'host_phone': entry.host.phone_Number,
                'checkInTime': entry.checkInTime,
            }
        )
    # Paginator shows limited number of visitors
    paginator = Paginator(runningMeetings, 6)
    page = request.GET.get('page')
    running_Meetings = paginator.get_page(page)

    context = {
        'title': "Current Meetings",
        'visitors': running_Meetings,
    }
    return render(request, 'host/runningMeetings.html', context)
