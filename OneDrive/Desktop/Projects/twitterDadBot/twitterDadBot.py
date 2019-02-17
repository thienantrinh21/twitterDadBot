import tweepy
import time

consumer_key = 'insert consumer key here'
consumer_secret = 'insert consumer secret key here'
access_token = 'insert access token here'
access_token_secret = 'insert access token secret here'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

Family = {}

while True:
    searchTweets = api.search("\"I\'m\"")
    #Searches the global twitter feed for tweets with the keyword "I'm"

    child = searchTweets[0].user.screen_name
    #Grabs the username of the latest tweet that meets the above criteria


    if child not in Family:
        #Ensures that the tweeter has never been tweeted at before

        Tweet = str(searchTweets[0].text.lower().replace("’","'"))

        # Stores the first tweet found in searchTweets
        # replaces all apostrophes to be matching since Twitter uses different types of apostrophes

        childsNameSplitter = Tweet.split("i'm ",1)
        #splits the tweet string into two elements in an array
        #the zeroth index is everything before the keyword "i'm" and the first index is everything after the keyword "i'm"

        childsName = childsNameSplitter[1]

        api.update_status(f"Hello \"{childsName}\", my name is Dad!", searchTweets[0].id)

        Family[child] = 1
        #Adds the username of the tweet to the family so that they will not be tweeted at agains 

    time.sleep(60)
