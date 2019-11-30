from django.shortcuts import render, redirect
from .forms import EntryForm
from .models import Visitor
from host.models import Host
from . import forms
from django.contrib import messages
from host import send_sms
from django.core.mail import send_mail
from django.conf import settings


# Handles route '/'
# Displays homepage
def Home(request):
    context = {
        'title': 'Home Page',
    }
    return render(request, 'visitor/home.html', context)


# Handles route '/schedule-a-meeting/'
# Takes visitor's and host's details to book a meeting
def schedule_a_meeting(request):
    if request.method == "GET":
        form = EntryForm()
        context = {
            'title': "Schedule A Meeting", 
            'form': form,
        }
        return render(request, 'visitor/scheduleAMeeting.html', context)
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            host = form.cleaned_data['host_name']
            host = Host.objects.filter(pk=host).first()
            newVisitor = Visitor.objects.create(
                first_name=form.cleaned_data['First_name'],
                last_name=form.cleaned_data['Last_name'],
                email=form.cleaned_data['Email'],
                phone_Number=form.cleaned_data['Phone_number'],
                address_Visited=form.cleaned_data['Address_visited'],
                host=host
            )
            newVisitor.save()

            msg = f"Your meeting is scheduled with " + \
                f"{newVisitor.first_name} \n" + \
                f"Visitor email: {newVisitor.email} \n" + \
                f"Visitor Phone {newVisitor.phone_Number} \n"
            print(host.user.email)
            try:
                send_mail(
                    'Meeting Scheduled',
                    msg,
                    settings.EMAIL_HOST_USER,
                    [host.user.email]
                )  # Sends mail to host
                print(host.user.email)
                sendSms(msg, host.phone_Number)  # Sends sms to host
            except:
                return redirect('websiteHome')
        else:
            # If form is not valid then return to same page
            # with an error message
            messages.info(request, 'Please enter valid details')
            return redirect('schedule-a-meeting')
        return redirect("websiteHome")


# Handles route '/checkout/'
# Takes details of visitor to check out
def checkout(request):
    # Find the user from db and redirect to
    # confirm-checkout page with his details
    if request.method == 'POST':
        checkoutForm = forms.CheckoutForm(request.POST)
        if checkoutForm.is_valid():
            visitor_fname = checkoutForm.cleaned_data["first_Name"]
            visitor_phone = checkoutForm.cleaned_data["phone_Number"]

            visitor = Visitor.objects.filter(
                first_name=visitor_fname,
                phone_Number=visitor_phone,
                is_checked_in="Yes"
            ).first()

            if visitor:
                id = visitor.pk
                return redirect("checkout-visitor", visitor_id=id)
            else:
                messages.info(request, 'No such visitor exist')
                return redirect('checkout')
        else:
            messages.info(request, 'Please enter valid details')
            return redirect('checkout')
    else:
        checkoutForm = forms.CheckoutForm()  # Create an empty checkout form
        context = {
            'form': checkoutForm,
            'title': "checkout"
        }
        return render(request, 'visitor/checkout.html', context)


# Handles route '/checkout/<int:visitor_id>/'
# Verifies visitor details before checkout
def checkoutVisitor(request, visitor_id):
    # Find the user from db and mark is_checked_in to 'No'
    if request.method == 'GET':
        visitorCheckoutForm = forms.CheckoutConfirmForm()
        visitor = Visitor.objects.filter(pk=visitor_id).first()
        host = Host.objects.filter(pk=visitor.host.pk).first()
        context = {
            'checkoutForm': visitorCheckoutForm,
            'title': "checkout",
            'visitor': visitor,
            'host': f"{host.user.first_name} {host.user.last_name}",
        }
        return render(request, 'visitor/checkoutVisitor.html', context)
    else:
        visitorCheckoutForm = forms.CheckoutConfirmForm(request.POST)
        if visitorCheckoutForm.is_valid():
            didCheckedOut = visitorCheckoutForm.\
                cleaned_data['Do_You_Want_To_Check_Out']

            # In case same user registers multiple times
            # then use the first details
            visitor = Visitor.objects.filter(pk=visitor_id).first()

            if didCheckedOut:
                visitor.is_checked_in = 'No'
            else:
                visitor.is_checked_in = 'Yes'

            visitor.save()  # Update visitor to db

            host = f"{visitor.host.user.first_name} {visitor.host.user.last_name}"

            msg = f"Your meeting is complete. Here are the details: \n" + \
                f"Name: {visitor.first_name} {visitor.last_name} \n" + \
                f"Email: {visitor.email} \n" + \
                f"Phone: {visitor.phone_Number} \n" + \
                f"Host: {host} \n" + \
                f"Address Visited: {visitor.address_Visited} \n"

            try:
                send_mail(
                    'You Checked Out',
                    msg,
                    settings.EMAIL_HOST_USER,
                    [visitor.email]
                )  # Sends mail to visitor

                sendSms(msg, visitor.phone_Number)  # Sends sms to visitor
            except:
                return redirect('websiteHome')
        return redirect('websiteHome')
