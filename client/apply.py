import stashshare
import requests
import sys

patch = requests.get("https://us-central1-stash-share.cloudfunctions.net/getPatch", {"name": sys.argv[1]}).json()['patch']
stashshare.apply(str.encode(patch))
