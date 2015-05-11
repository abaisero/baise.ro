from fabric.api import *
from datetime import datetime
from slugify import slugify
import os
import fabric.contrib.project as project
import string

# PROD = 'sjl.webfactional.com'
# DEST_PATH = '/home/sjl/webapps/slc/'
# ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
# DEPLOY_PATH = os.path.join(ROOT_PATH, 'deploy')

def clean():
    # local('rm -rf ./deploy')
    # local('rm -rf ./_site')
    pass

def build():
    # clean()
    local('jekyll build --watch')

def serve():
    local('jekyll serve')

def post(title='New Post'):
    # date = datetime.now().strftime('%Y-%m-%d')
    date = datetime.now().strftime('%F')
    fname = '_posts/' + date + '-' + slugify(title) + '.md'
    front_matter = '"+normal i---kjotitle: ' + string.capwords(title) + 'kjodescription:kjo---" ' if not os.path.isfile(fname) else ''
    command = 'vim ' + front_matter + fname
    local('vim ' + front_matter + fname)

def page(title='New Page'):
    fname = slugify(title) + '.md'
    front_matter = '"+normal i---" "+normal otitle: ' + string.capwords(title) + '" "+normal olayout: default" "+normal o---" ' if not os.path.isfile(fname) else ''
    command = 'vim ' + front_matter + fname
    local('vim ' + front_matter + fname)


# def reserve():
#     regen()
#     serve()

# def smush():
#     local('smusher ./media/images')

# @hosts(PROD)
# def publish():
#     regen()
#     project.rsync_project(
#         remote_dir=DEST_PATH,
#         local_dir=DEPLOY_PATH.rstrip('/') + '/',
#         delete=True
#     )
