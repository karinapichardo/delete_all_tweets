# This script will delete all of the tweets in the specified account.
# You may need to hit the 'more' button on the bottom of your twitter profile
# page every now and then as the script runs, this is due to a bug in twitter.

import twitter # Requires python-twitter library

username = 'your_username'
password = 'your_password'
count = 200 # Number of statuses in a batch. Twitter API wont allow more than 200

api = twitter.Api(username=username, password=password)
api.SetCache(None) # Caching needs to be turned off

def delete_tweet(status_id):
    """Deletes tweet with matching status_id"""
    api.DestroyStatus(status_id)
    print "Deleted: " + str(status_id)

batch = 0 # initialise batch counter
while True: # Rinse and repeat
    batch += 1 # Increment batch counter
    print "\nProcessing batch " + str(batch)
    tweets = api.GetUserTimeline(username, count=count) # Get batch of tweets
    if not tweets: break # Exit if there aren't any tweets left
    [delete_tweet(tweet.id) for tweet in tweets] # Delete tweets in this batch
   
print "\nDone"
