# -*- coding: utf-8 -*-
#!/usr/bin/env python

import oauth2
import os

def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    print key
    print secret
    print CONSUMER_KEY
    print CONSUMER_SECRET

    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content

CONSUMER_KEY=os.environ['CONSUMER_KEY']
CONSUMER_SECRET=os.environ['CONSUMER_SECRET']
ACCESS_TOKEN=os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET=os.environ['ACCESS_TOKEN_SECRET']

home_timeline = oauth_req( 'https://api.twitter.com/1.1/statuses/home_timeline.json', ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
print home_timeline
