import requests
import json
import urllib.request

nasa_api = "C6WdSznk583MreQYT0SUmBS4a4p1KPpM2cAsyLO3"
ipstack_key = "5b5e944af6a945e4e0891c4836b4b9d4"

location_url_api = "http://api.ipstack.com/check?access_key=%s"
nasa_url_api = "https://api.nasa.gov/planetary/apod?api_key=%s"


class Api:

    def __init__(self, access_key,url_addres):
        self.access_key = access_key
        self.url_addres = url_addres

    def getting_api(self):
        location_url = self.url_addres % (self.access_key)
        r = requests.get(location_url)
        j = json.loads(r.text)
        return j



api1 = Api(ipstack_key,location_url_api)
lat = api1.getting_api()['latitude']
lon = api1.getting_api()['longitude']
print(lat,lon)

api2 = Api(nasa_api,nasa_url_api)
title_galaxy = api2.getting_api()["title"]
date = api2.getting_api()["date"]
image = urllib.request.urlretrieve(api2.getting_api()["url"],"%s_%s.jpg" % (title_galaxy,date))







