from twitterService import sendTweet
from covidStatusService import getRSCovidStatuses
import schedule
import time

def sendCovidUpdates():
    statuses = getRSCovidStatuses()

    for status in statuses:
        title = status['titulo']
        flag = status['bandeira']
        description = status['bandeira_descricao']
        tweet = title + ' está na bandeira '+flag+'. \nDescrição: '+description

        sendTweet(tweet)
schedule.every(1).minutes.do(sendCovidUpdates)

while True:
    schedule.run_pending()
    time.sleep(1)