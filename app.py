from twitterService import sendTweet
from covidStatusService import getRSCovidStatuses
import time
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval',minutes=1)
def sendCovidUpdates():

    print('Starting to send out updates!')
    statuses = getRSCovidStatuses()
    print('Statuses retrieved!')
    for status in statuses:
        title = status['titulo']
        flag = status['bandeira']
        description = status['bandeira_descricao']
        print('  Sending update for '+title)
        tweet = title + ' está na bandeira '+flag+'. \nDescrição: '+description

        sendTweet(tweet)
    

    # Current date time in local system
    print(datetime.now())
    print('All updates sent!')

sched.start()