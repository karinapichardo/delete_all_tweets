# -*- coding: utf-8 -*-
"""
@requirements: python-twitter (http://code.google.com/p/python-twitter/) and simplejson (http://code.google.com/p/simplejson/)
@author: Dave Jeffery

This script will delete all of the tweets in the specified account.
You may need to hit the "more" button on the bottom of your twitter profile
page every now and then as the script runs, this is due to a bug in twitter.
"""
 
import twitter, urllib2

def delete_tweet(api, status_id):
    """Deletes tweet with matching status_id"""
    api.DestroyStatus(status_id)
    print "Deleted:", status_id
 
def batch_delete(username, password, batch_size=200):
    """Fetches tweets in batches and calls delete_tweet on each one"""
    api = twitter.Api(username, password)
    api.SetCache(None) # Caching needs to be turned off
    
    print "Deleting all tweets from", username
    batch = 0
    while True: # Rinse and repeat
        tweets = api.GetUserTimeline(username, count=batch_size) # Get batch of tweets
        if tweets:
            batch += 1
            print "\nProcessing batch", batch
            for tweet in tweets:
                delete_tweet(api, tweet.id)
        elif not tweets:
            print "\nNo tweets left... Done"
            break

if __name__ == "__main__":      
    batch_delete(username="user", password="pass")