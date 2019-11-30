# Entry Management Software

This application helps to keep track of large number of visitors and their meeting details.

## Features

The whole application is divided into two parts.
* One section is for Visitor and another one is for Host

#### In Visitor Section
* Meeting Scheduler (Schedule a Meeting)
* Visitors Checkout (Checkout)
If a visitor wants to meet a person, he will enter his details and select the host in "Schedule a Meeting" section.  
Then host will receive a mail and sms about the scheduled meeting.  

When the visitor will checkout then he will receive a mail and sms about the meeting.  

#### In Host Section
* Login and Register Host
* See Currently Running Meetings and Previous Meetings

## Requirements

* Python 3.x

### Built With

* Frontend - HTML, CSS, Javascript
* Backend - Django v 2.2.7
* Database used for testing - sqlite
For using any other database please visit the django documemtation page for further details.
Link - https://docs.djangoproject.com/en/2.2/ref/databases/

## Note:

* This app uses twilio for sending sms and gmail for sending mails.  
* For gmail dummy email has been created and credentials have been updated.  
* For sms functionality to work please update twilio auth_token and account_sid in entryManagement/settings.py the sms functionality won't work.  
* It's always recommended to use environment variables for saving credentials.  
* Save the credentials like `ACCOUNT_SID`, `AUTH_TOKEN`, `EMAIL_HOST_PASSWORD` and `SECRET_KEY` in the environment variables.  
* Also for testing `DEBUG` was set to `True`. In `settings.py` set `DEBUG = False` otherwise it may show some important details in the browser.

## Project Folder Structure
```
├── README.md
├── db.sqlite3
├── entryManagement
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── host
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── send_sms.py
│   ├── static
│   │   └── host
│   │       └── main.css
│   ├── templates
│   │   └── host
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── logout.html
│   │       ├── previousMeetings.html
│   │       ├── register.html
│   │       └── runningMeetings.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── visitor
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations
    │   ├── 0001_initial.py
    │   └── __init__.py
    ├── models.py
    ├── static
    │   ├── assets
    │   │   └── background.png
    │   └── visitor
    ├── templates
    │   └── visitor
    │       ├── checkout.html
    │       ├── checkoutVisitor.html
    │       ├── home.html
    │       └── scheduleAMeeting.html
    ├── tests.py
    ├── urls.py
    └── views.py
```

## How to run?
* Create a virtual environment using `python3 -m venv myvenv`
* Activate the virtual environment using `source myvenv/bin/activate` command
* Create a project folder and inside the project folder clone the repository using `https://github.com/raj09utkarsh/Innovacer-Entry-Management.git`
* `cd Innovacer-Entry-Management`
* Install the dependencies using `pip3 install -r requirements.txt`
* `cd entryManagement`
* Optional - Open `settings.py` from `entryManagement/entryManagement/` directory and update your credentials for gmail and twillio login. 
Now use the following commands to run the app -
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
* Open `http://localhost:8000/` in your browser to see the results.

## Results and Screenshots

### Homepage
http://localhost:8000/
![Homepage](screenshots/websiteHome.png?raw=true)

### Schedule a Meeting
http://localhost:8000/schedule-a-meeting/
![Schedule a Meeting](Screenshots/schedule1.png.png?raw=true)

Schedule a meeting - continued
![Schedule a Meeting](Screenshots/schedule2.png.png?raw=true)

### Email output for scheduled meeting
![Output](Screenshots/email-meeting-scheduled.png?raw=true)

### SMS output for scheduled meeting
![Output](Screenshots/meetingScheduled.png?raw=true)

### Checkout
http://localhost:8000/checkout/
![Checkout](Screenshots/checkout.png?raw=true)

### If wrong details are entered while checkout
![Checkout](Screenshots/wrong-checkout.png?raw=true)

### Confirm Checkout
![Checkout](Screenshots/confirm-checkout.png?raw=true)

### Checkout email output
![Checkout](Screenshots/email-output-complete.png?raw=true)

### Checkout sms output
![Checkout](Screenshots/meetingComplete.png?raw=true)

### Host Dashboard
http://localhost:8000/host/
![Running Meetings](Screenshots/hostdashboard.png?raw=true)

### Running Meetings
http://localhost:8000/running-meetings/
![Running Meetings](Screenshots/running-meetings.png?raw=true)

### Past Meetings
http://localhost:8000/past-meetings/
![Past Meetings](Screenshots/past-meetings.png?raw=true)


#### Thanks