import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

'#I used this method because I am having a problem to enable my Google Maps API key'


def get_information(address):
    api_key = False
    if api_key is False:
        api_key = 42
        service_url = 'https://py4e-data.dr-chuck.net/json?'
    else:
        service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    contex_ssl = ssl.create_default_context()
    contex_ssl.check_hostname = False
    contex_ssl.verify_mode = ssl.CERT_NONE
    address_location = address
    parameters = dict()
    parameters['address'] = address_location
    if api_key is not False:
        parameters['key'] = api_key
    url = service_url + urllib.parse.urlencode(parameters)
    uh = urllib.request.urlopen(url, context=contex_ssl)
    data = uh.read().decode()
    response = json.loads(data)
    location = response['results'][0]['formatted_address']
    return location
