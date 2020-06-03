
from twitterService import sendTweet
from covidStatusService import getRSCovidStatuses

statuses = getRSCovidStatuses()

for status in statuses:
    title = status['titulo']
    flag = status['bandeira']
    description = status['bandeira_descricao']
    tweet = title + ' está na bandeira '+flag+'. Descrição: '+description

    sendTweet(tweet)
    break