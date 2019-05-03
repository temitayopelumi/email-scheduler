#sending scheduled emails

import sendgrid
import os
from sendgrid.helpers.mail import *
import urllib
import  requests
import json
from apscheduler.schedulers.blocking import BlockingScheduler

#function to get quote from an api
def quotes():
    try:
        h="https://favqs.com/api/qotd"
        response=requests.get(h)
        res=response.json()
        return (res['quote']['body'])
    except:
        print("connection error")

#scheduled email using apscheduler decorators.
sched=BlockingScheduler()
@sched.scheduled_job("cron", day_of_week='*', hour=12)

#function to send quotes using sendgrid 
def send_quotes():
    sg = sendgrid.SendGridAPIClient(os.environ.get("fess"))
    data={"personalizations":[{
            "to":[{"email":"pelumi085@gmail.com"}],
            "subject":"qutoes"},
                
            {"to":[{"email":"dammy025@gmail.com"}],
            "subject":"quotes"},
            {"to":[{"email":"chisomokafor1999@gmail.com"}],
            "subject":"quotes"},
            {"to":[{"email":"dowolebolu@gmail.com"}],
            "subject":"quotes"}],
            "from":{"email":"olalekantemitayo7@gmail.com"},
            "content":[{"type":"text/plain","value":quotes()}]
            }
    try:
        response = sg.client.mail.send.post(request_body=data)
        if response.status_code==202:
            print("Message sent")
        else:
            print("Message not sent")
    except:
        print("Connection error")
    
    
sched.start()



