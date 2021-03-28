import requests
import json
import urllib.request

nasa_api = "C6WdSznk583MreQYT0SUmBS4a4p1KPpM2cAsyLO3"

def getting_nasa(access_key):
    nasa_url = "https://api.nasa.gov/planetary/apod?api_key=%s" % (access_key)
    r = requests.get(nasa_url)
    j = json.loads(r.text)
    return  j




#nasa news
nasa = getting_nasa(nasa_api)
for x in nasa:
    print(x , " -", nasa[x])
# title_galaxy = nasa["title"]
# date = nasa["date"]
# image = urllib.request.urlretrieve(nasa["url"],"%s_%s.jpg" % (title_galaxy,date))
