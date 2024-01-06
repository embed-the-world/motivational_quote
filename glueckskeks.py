import requests
import json

def get_quote():
    return requests.get("https://zenquotes.io/api/random").json()

def print_quote(zenquote_return):
    quote = zenquote_return[0]["q"]
    author = zenquote_return[0]["a"]
    print (quote + " - by " + author)

if __name__ == "__main__":
    print_quote(get_quote())

