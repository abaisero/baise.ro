from fabric.api import *

env.user = 'bais'
env.hosts = 'ssh.pythonanywhere.com'

def deploy():
    print run('git -C $HOME/git/baise.ro pull')
