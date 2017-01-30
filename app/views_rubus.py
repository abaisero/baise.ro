################################################################################
# rubus public page
################################################################################

import os

from flask import g, request, render_template, redirect, abort, url_for, send_from_directory
from flask_wtf import Form
from wtforms import TextField, FileField, SubmitField
from werkzeug import secure_filename

from app import app
from db import User, session

from sqlalchemy import exists
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound


class RubusForm(Form):
    username = TextField('Username')
    file = FileField('File')
    submit = SubmitField('Submit')

# TODO check out what the extra hidden field is...

@app.route('/rubus/', methods=['GET', 'POST'])
def rubus():
    form = RubusForm(request.form)

    if request.method == 'POST' and form.validate():
        username = form.username.data
        reqfile = request.files[form.file.name]
        # TODO allowed_file / validation
        pic = secure_filename(reqfile.filename)
        return redirect(url_for('user_pic', username=username, pic=pic), code=307)

    # rubus = app.config['RUBUS_PATH']

    users = {}
    for user in session.query(User).all():
        user_pix_path = app.config['RUBUS_PATH'] / user.username
        # TODO use the DB here...
        try:
            users[user.username] = [p.name for p in user_pix_path.iterdir()]
        except OSError:
            pass

    return render_template('rubus.html', form=form, users=users)


################################################################################
# RESTful rubus API
################################################################################


from flask_restful import Api, Resource
api = Api(app)

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    user = session.query(User).filter(User.username == username).first()
    if user is None or user.password != password:
        return False
    g.user = user
    return True

@auth.error_handler
def auth_error():
    return abort(401)

# DB query help functions
def _user_or_abort(username, code=404):
    try:
        user = session.query(User).filter(User.username == username).one()
    except (NoResultFound, MultipleResultsFound) as e:
        abort(code)
    return user

# engine = create_engine('sqlite:///app/rubus.db')
# from rubus_db import engine

def _user_path(username):
    return app.config['USERS_PATH'] / username

def _pic_path(username, pic):
    return _user_path(username) / pic


def test_auth():
    print request.json.get('username')
    print request.authorization


class UsersAPI(Resource):
    def get(self):
        test_auth()
        status = 'success'
        users = [user.as_json() for user in session.query(User.username).all()]
        data = dict(users=users)
        return dict(status=status, data=data)

    def post(self):
        if not request.is_json:
            abort(415)

        json = request.get_json()
        try:
            username = json['username']
            password = json['password']
        except KeyError:
            abort(400)

        if session.query(exists().where(User.username == username)).scalar():
            abort(422)

        session.add(User(username=username, password=password))
        session.commit()

        return url_for('user', username=username, _external=True)


class UserAPI(Resource):
    def get(self, username):
        user = _user_or_abort(username)
        status = 'success'
        data = dict(user=user.as_json())
        return dict(status=status, data=data)

    def delete(self, username):
        if not request.is_json:
            abort(415)
        
        json = request.get_json()
        try:
            username = json['username']
            password = json['password']
        except KeyError:
            abort(400)

        # TODO bug, I am overwriting the username! not the same as in url

        user = _user_or_abort(username)
        if user.password != password:
            abort(403)

        session.delete(user)
        session.commit()


class UserFriendsAPI(Resource):
    # NOTE I THINK THIS IS THE ONLY CORRECT ONE
    @auth.login_required
    def get(self, username):
        if g.user.username != username:
            abort(403) # TODO change error code
        status = 'success'
        data = dict(user=g.user.as_json(with_friends=True))
        return dict(status=status, data=data)

    # PUT method in UserFriendAPI seems cleaner
    # def post(self, username):
    #     if not request.is_json:
    #         abort(415)

    #     json = request.get_json()
    #     try:
    #         friend_username = json['friend_username']
    #     except KeyError:
    #         abort(400)
        
    #     user = _user_or_abort(username)
    #     friend = _user_or_abort(friend_username)

    #     if friend in user.friends:
    #         abort(400)  # TODO check code..

    #     user.befriend(friend)
    #     session.commit()


class UserFriendAPI(Resource):
    # TODO no need for get here..
    # def get(self, username, friendname):
    #     user = _user_or_abort(username)
    #     friend = _user_or_abort(friendname)

    #     if friend not in user.friends:
    #         abort(404)

    #     status='success'
    #     data = dict(friend=_user_json(friend))
    #     return dict(status=status, data=data)
    #     # TODO

    def put(self, username, friendname):
        user = _user_or_abort(username)
        friend = _user_or_abort(friendname)

        user.befriend(friend)
        session.commit()

        status = 'success'
        data = None
        return dict(status=status, data=data)

    def delete(self, username, friendname):
        user = _user_or_abort(username)
        friend = _user_or_abort(friendname)

        user.unfriend(friend)

        status = 'success'
        data = None
        return dict(status=status, data=data)


class UserPixAPI(Resource):
    def get(self, user):
        _user_or_abort(user)
        user_path = _user_path(user)
        pix_hrefs = [url_for('user_pic', user=user, pic=pic_path.name, _external=True) for pic_path in user_path.iterdir()]
        hrefs = dict(rel='self', href=pix_hrefs)
        return dict(username=user, hrefs=hrefs)


class UserPicAPI(Resource):
    def get(self, user, pic):
        _user_or_abort(user)

        user_dir = str(_user_path(user))
        return send_from_directory(user_dir, pic)
    
    # TODO move post to UserPixAPI
    def post(self, user, pic):
        _user_or_abort(user)
        pic_path = _pic_path(user, pic)

        reqfile = request.files['file']
        reqfile.seek(0, 2)
        MB = reqfile.tell() / 1024. / 1024.
        try:
            pic_path.parent.mkdir(parents=True)
        except OSError: 
            pass
        finally:
            reqfile.save(str(picpath))

        pic_href = url_for('user_pic', user=user, pic=pic, _external=True)
        hrefs = dict(rel='self', href=pic_href)

        def _user_pic_href(user, pic):
            return dict(rel='self', href=url_for('user_pic', user=user, pic=pic, _external=True))

        hrefs = [ _user_pic_href(user, pic) ]
        return dict(user=user, pic=pic, hrefs=hrefs)

    def delete(self, user, pic):
        _user_or_abort(user)
        pic_path = _pic_path(user, pic)

        try:
            pic_path.unlink()
        except OSError:
            abort(404)
        return dict(result=True)


# TODO cool way to login user
# TODO RESTful guideline and return json format
# TODO don't login the friend for now?


api.add_resource(UsersAPI,       '/rubus/api/v0/users/',                         endpoint='users')
api.add_resource(UserAPI,        '/rubus/api/v0/users/<username>/',                  endpoint='user')
api.add_resource(UserFriendsAPI, '/rubus/api/v0/users/<username>/friends/',          endpoint='user_friends')
api.add_resource(UserFriendAPI,  '/rubus/api/v0/users/<username>/friends/<friendname>/', endpoint='user_friend')
api.add_resource(UserPixAPI,     '/rubus/api/v0/users/<username>/pix/',              endpoint='user_pix')
api.add_resource(UserPicAPI,     '/rubus/api/v0/users/<username>/pix/<pic>/',        endpoint='user_pic')

# TODO always use SSL

# TODO check file size
# TODO check if file already exists

# TODO use vnc stuff to connect to any android device! no need for external screen!
