import stashshare
import requests

patch = requests.get("https://us-central1-stash-share.cloudfunctions.net/getPatch", {"name": "blue mob"}).json()['patch']
stashshare.apply(str.encode(patch))