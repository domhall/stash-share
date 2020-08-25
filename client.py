import stashshare
import requests

def send_changes():
    patch = stashshare.save()
    r = requests.post("https://us-central1-stash-share.cloudfunctions.net/sendPatch", json =
    {
        'name': 'blue mob',
        'patch': patch
    })
    print(r.text)


def receive_changes():
    patch = 'get patch here'
    stashshare.apply(patch)

def test_endpoint():
    r = requests.post("https://us-central1-stash-share.cloudfunctions.net/sendPatch", json =
    {
        'name': 'blue mob',
        'patch': b'test'
    })
    print(r.json()['_path']['segments'][1])

test_endpoint()