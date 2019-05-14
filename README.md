###Email-scheduler
This is an email scheduler written for sending quotes to specified mails using Sendgrid Api. It is hosted on heroku.
*requirements*
-APScheduler
-Sendgrid
-any quote api
-gmail account
-python 2.7,3.5+
-heroku account and cli
*usage*
-clone the files on this repository to your local machine.
-create the sendgrid account and get your api key needed for sending the the mail.
-create the heroku account and download the heroku cli.
-create an app on heroku,follow the steps for deployment of an app.
-lastly scale your dyno as follows: heroku ps:scale clock=1.
*project files*
grid.py             #python file that does the scheduling, sending of mails and getting the api.
Procfile            #specifies the dyno you are using, to be deployed to heroku.
requirements.txt    #the dependencies of the app,also to be uploaded to heroku.
runtime.txt         #specifies the version of python you are using.


