# git stash show -p > patch

# git apply patch
# git stash
import subprocess

def save():
    subprocess.Popen(['git', 'stash']).wait()
    p = subprocess.Popen(['git', 'stash', 'show', '-p'],
                     stdout=subprocess.PIPE)
    patch, _ = p.communicate()
    subprocess.Popen(['git', 'stash', 'apply']).wait()
    return patch

def apply(patch):
    p = subprocess.Popen(['git', 'apply'], stdin=subprocess.PIPE)
    p.communicate(patch)