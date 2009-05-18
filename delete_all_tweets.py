# This script will delete all of the tweets in the specified account.
# You may need to hit the 'more' button on the bottom of your twitter profile
# page every now and then as the script runs, this is due to a bug in twitter.
 
import twitter # Requires python-twitter library
 
username = 'your_username'
password = 'your_password'
 
api = twitter.Api(username=username, password=password)
api.SetCache(None) # Caching needs to be turned off

def delete_tweet(status_id):
    """Deletes tweet with matching status_id"""
    api.DestroyStatus(status_id)
    print "Deleted:", status_id
 
def batch_delete(batch_size = 200, username = username):
    """Fetches tweets in batches and calls delete_tweet on each one"""
    print "Deleting all tweets from", username
    batch = 0
    while True: # Rinse and repeat
        
        tweets = api.GetUserTimeline(username, count=batch_size) # Get batch of tweets
        
        if tweets:
            batch += 1 # Increment batch counter
            print "\nProcessing batch", batch
            for tweet in tweets:
                delete_tweet(tweet.id)
        else: # Exit if there aren't any tweets left
            print "\nNo tweets left... Done"
            break

batch_delete()