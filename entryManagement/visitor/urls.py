# This file contains url patterns for visitor app

from django.urls import path, include
from . import views


urlpatterns = [
    # / 
    path('', views.Home, name="websiteHome"),

    # /schedule-a-meeting/
    path('schedule-a-meeting/', \
        views.schedule_a_meeting, \
        name="schedule-a-meeting"
    ),

    # /checkout/visitor_id/
    path('checkout/<int:visitor_id>/', \
        views.checkoutVisitor, \
        name="checkout-visitor"
    ),

    # /checkout/
    path('checkout/', \
        views.checkout, \
        name="checkout"
    ),
]
