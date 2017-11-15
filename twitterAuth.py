#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-authorize:
#  - step through the process of creating and authorization a
#    Twitter application.
#-----------------------------------------------------------------------

import twitter
import time

# consumer_key = 'zlHSEOcRXszheIurATDbV2oUl'
# consumer_secret = '8H7oIwJgfF5S8OMtvMn5VWITTIiYSmBCrv4g8HVWgV5pUGSpkd'
# access_key = '122389961-rt1AkthMjlAEb6RbDpUo8GvfopYYfDLCpQDchAFN'
# access_secret = 'PXI7KLYGy33WmrnaxHzFJmw79N9yH5PgAIFyD52IDNNUD'


print "1. Create a new Twitter application here: https://apps.twitter.com"
print "When you have created the application, enter:"
print "   your application name: ",
app_name = 'PythonAppSiraj'

print "   your consumer key: ",
consumer_key = 'zlHSEOcRXszheIurATDbV2oUl'

print "   your consumer secret: ",
consumer_secret = '8H7oIwJgfF5S8OMtvMn5VWITTIiYSmBCrv4g8HVWgV5pUGSpkd'

print "2. Now, authorize this application."
print "You'll be forwarded to a web browser in two seconds."
print

time.sleep(2)

access_key, access_secret = twitter.oauth_dance(app_name, consumer_key, consumer_secret)

print "Done."
print
print "Now, replace the credentials in config.py with the below:"
print
print "consumer_key = '%s'" % consumer_key
print "consumer_secret = '%s'" % consumer_secret
print "access_key = '%s'" % access_key
print "access_secret = '%s'" % access_secret