import subprocess

def save():
    p = subprocess.Popen(['git', 'diff'],
                     stdout=subprocess.PIPE)
    patch, _ = p.communicate()
    return patch

def apply(patch):
    subprocess.Popen(['git', 'reset', '--hard']).wait()
    p = subprocess.Popen(['git', 'apply'], stdin=subprocess.PIPE)
    p.communicate(patch)
