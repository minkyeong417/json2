import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    '''
    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    '''
    url = ' http://py4e-data.dr-chuck.net/comments_348559.json'
    #print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read().decode()
    #print('Retrieved', len(data), 'characters')
    #print(data.decode())
    #tree = ET.fromstring(data)
    '''
    results = tree.findall('comments/comment')
    sum = 0
    for comment in results:
        sum = sum + int(comment.find('count').text)
    '''
    js = json.loads(data)
    break

'''data =
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

#info = json.loads(data)
#print('User count:', len(info))
sum = 0
for item in js['comments']:
    sum = sum + item['count']
print(sum)
