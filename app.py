from twitterService import sendTweet
from covidStatusService import getRSCovidStatuses
import time
from datetime import datetime
import tweepy

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron',id='covid_update',day_of_week='sun')
def sendCovidUpdates():

    print('Starting to send out updates!')
    statuses = getRSCovidStatuses()
    print('Statuses retrieved!')
    for status in statuses:
        title = status['titulo']
        flag = status['bandeira']
        print('  Sending update for '+title)
        tweet = title + ' está na bandeira '+flag
        print(tweet)
        tweet = tweet[0:263]+' #covid #rs #covidrs'

        now = datetime.now() # current date and time

        currentDate=now.strftime("%d/%m/%Y")

        tweet = currentDate+'\n '+tweet
        
        time.sleep(60)
        try:
            sendTweet(tweet)
        except tweepy.error.TweepError:
            print('Erro sending out tweet... duplicate')
        except Exception as e:
            print('Failed to upload to ftp: '+ str(e))

    # Current date time in local system
    print(datetime.now())
    print('All updates sent!')

sched.start
# sendCovidUpdates()