from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


# contains all urlpatterns for 'host/'
urlpatterns = [
    # /host/ 
    path('', views.Home, name="hostHome"),

    # /host/register/
    path('register/', views.HostRegister, name="hostRegister"),

    # /host/login/
    path('login/', \
        auth_views.LoginView.as_view(template_name='host/login.html'),\
        name="hostLogin"
    ),

    # /host/logout/
    path('logout/', \
        auth_views.LogoutView.as_view(template_name='host/logout.html'), \
        name="hostLogout"
    ),

    # /host/running-meetings/
    path('running-meetings/', \
        views.runningMeetings, \
        name="running-meetings"
    ),

    # /host/past-meetings/
    path('past-meetings/', \
        views.pastMeetings, \
        name="past-meetings"
    ),
]
