import tweepy
import csv

#key = key
#secret = secret
#consumer_key = consumer_key
#consumer_secret = consumer_secret

class MyStreamListener(tweepy.StreamListener):

    numTweets = 1

    def on_status(self, status):
        if 'RT @' not in status.text:
            try:
                with open('Data.csv', 'a', newline='') as file:
                    f = csv.writer(file, dialect='excel', delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    f.writerow([status.text])
                    print(self.numTweets)
                    self.numTweets = self.numTweets + 1
            except UnicodeEncodeError:
                print("emoji")
        else:
            print("retweet")

    def on_error(self, status_code):
        return super().on_error(status_code)


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(key, secret)
    auth.set_access_token(consumer_key, consumer_secret)

    api = tweepy.API(auth)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

    myStream.filter(languages=["en"], track=["the", "i", "to", "a", "and", "is", "in", "it", "you", "of"])