import stashshare
import requests

patch = stashshare.save().decode("utf-8")
r = requests.post("https://us-central1-stash-share.cloudfunctions.net/sendPatch", json =
{
    'name': 'blue mob',
    'patch': patch
})
# print(r.text)
# print(r)