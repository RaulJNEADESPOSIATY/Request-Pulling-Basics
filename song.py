import requests
import random

import json

name = input("enter a band ")


response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + name)

# print(json.dumps(response.json()))


o = response.json()
for i in o["results"]:
    print(i["trackName"])


name_1 = input("enter name of a band ")

hello = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" +name_1)

yes = hello.json()
for x in yes["results"]:
    print(x["trackName"])



name_2  = input("pleas enter a name ")

nope = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" +name_2)

noe = nope.json()
for h in noe["results"]:
    print(h["trackName"])

name_22 = input("enter an artist ")
yes = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" +name_22)

nice = yes.json()
for l in nice("results"):
    print(l["trackName"])