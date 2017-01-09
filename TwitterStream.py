from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey                       = 'tBk723ZWpFxJAHTgCHuOuJIVb'
csecret                    = '2JMw6tkIq23Tp4brZHCTushPlJplDiDvqd4z0A6L6SEIX4L1MQ'
atoken                     = '2778557011-qhDPa76iHe7iAvVB1IFY4U1bYb3jK7HaVeAYbQX'
asecret                    = 'ktnBpgr86Yl7ZB4QTTnyABmfbeyGvnG4GTAwxjUKmGfVc'


class listener(StreamListener):
    def on_data(self, data):
        try:
            tweet          = data.split(',"text":"')[1].split('","source')[0]
            print tweet

            saveThis       = str(time.time()) + '::' + tweet
            savefile       = open('twitDb.csv', 'a')
            savefile.write(data)
            savefile.write('\n')
            savefile.close()
            return True

        except BaseException, e:
            print 'failed ondata,',str(e)
            time.sleep(5)


def on_error(self, status):
    print(status)

auth                       = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream              = Stream(auth, listener())
twitterStream.filter(track = ["new year"])
