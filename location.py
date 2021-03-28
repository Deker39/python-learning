import requests
import json
import urllib.request

ipstack_key = "5b5e944af6a945e4e0891c4836b4b9d4"

def getting_location(access_key):
    location_url = "http://api.ipstack.com/check?access_key=%s" % (access_key)
    r = requests.get(location_url)
    j = json.loads(r.text)
    print(j)
    for x in j:
        print("%s - %s" % (x, j[x]))
    # lat = j['latitude']
    # lon = j['longitude']
    return j

#my place
lacation= getting_location(ipstack_key)
lat = lacation['latitude']
lon = lacation['longitude']
print(lat,lon)