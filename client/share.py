import stashshare
import requests
import sys

patch = stashshare.save().decode("utf-8")
r = requests.post("https://us-central1-stash-share.cloudfunctions.net/sendPatch", json =
{
    'name': sys.argv[1],
    'patch': patch
})
