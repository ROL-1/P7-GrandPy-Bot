# import requests

# S = requests.Session()

# URL = "https://en.wikipedia.org/w/api.php"

# PARAMS = {
# "action": "query",
# "format": "json",
# "titles": "Wikimedia Foundation",
# "prop": "coordinates"
# }

# R = S.get(url=URL, params=PARAMS)
# DATA = R.json()
# PAGES = DATA['query']['pages']
# print(PAGES)

# for k, v in PAGES.items():
#     print("Latitute: " + str(v['coordinates'][0]['lat']))
#     print("Longitude: " + str(v['coordinates'][0]['lon']))

# -0.50, 44.80
# 37.7891838|-122.4033522

import requests

S = requests.Session()

URL = "https://fr.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "prop":"extracts|coordinates", # infos
    "explaintext":"1", # text or html (boolean y/n)
    "exintro": "1", # intro (boolean y/n)
    "format": "json",
    # "list": "geosearch",
    # "gscoord": "44.841225|-0.5800364",
    # "gslimit": "3",
    # "gsradius": "10000",
    "generator": "search", # how to search
    "gsrsearch": "pont bordeaux", # terms search
    "exsentences": "3", # nb sentences
    "gsrlimit":"1",  # nb results
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()
print(DATA)

# PLACES = DATA['query']['geosearch']

# for place in PLACES:
#     print(place['title'])