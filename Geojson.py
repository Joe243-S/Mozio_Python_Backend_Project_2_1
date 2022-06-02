import urllib.request, urllib.parse, urllib.error
import json
import ssl

#I used this method because I am problem to enable my API key

def getInformation(Address):
    api_key = False

    if api_key is False:
        api_key = 42
        serviceurl = 'http://py4e-data.dr-chuck.net/json?'

    else :
        serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    address = Address

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    js = json.loads(data)
    location = js['results'][0]['formatted_address']
    return location