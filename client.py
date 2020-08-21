import stashshare

def send_changes():
    patch = stashshare.save()


def receive_changes():
    patch = 'get patch here'
    stashshare.apply(patch)