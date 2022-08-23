import requests
import json

anfrage = requests.get("https://zenquotes.io/api/random").json()
quote = anfrage[0]["q"]
author = anfrage[0]["a"]
print (quote + " - by " + author)
