from twitterService import sendTweet
from covidStatusService import getRSCovidStatuses
import time
from datetime   import datetime
import tweepy

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

# @sched.scheduled_job('cron',id='covid_update',day_of_week='sun')
def sendCovidUpdates():

    print('Starting to send out updates!')
    statuses = getRSCovidStatuses()
    print(statuses)
    print('Statuses retrieved!')
    now = datetime.now() # current date and time
    currentDate=now.strftime("%d/%m/%Y")
    for status in statuses:
        list_of_statuses = statuses[status]
        city_statuses = list_of_statuses.cities
        name = list_of_statuses.name
        tweet = currentDate+' - '+status+'\n'
        for city_status in city_statuses:
            tweet = tweet + city_status['titulo']+','
            if(len(tweet) >= 230):
                print(len(tweet))
                tweet = tweet +' #covid #rs #covidrs'
                print(tweet)
                sendTweet(tweet)
                time.sleep(5)
                tweet = currentDate+' - '+status+'\n'
                
    print('All updates sent!')

# sched.start
sendCovidUpdates()