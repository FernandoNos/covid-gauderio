from twitterService import sendTweet
from covidStatusService import getRSCovidStatuses
import schedule
import time
from datetime import datetime

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
        break
    

    # Current date time in local system
    print(datetime.now())
    print('All updates sent!')
schedule.every(1).minutes.do(sendCovidUpdates)

while True:
    schedule.run_pending()
    time.sleep(1)