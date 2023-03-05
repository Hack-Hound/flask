
import flask_login as fl
from flask import Flask, request, render_template, redirect, url_for, session, flash, send_file
# from flask_socketio import SocketIO
from flask.views import *
from functools import wraps

# from server_pkg import crypto
from server_pkg.models import User

from urllib.parse import urlparse, urljoin


def UserUsernameByID(ID):
    return (User.query.filter_by(id=ID).first().username)


def UserDetailsByID(ID):
    return (User.query.filter_by(id=ID).all())


def AllUsersUserDetails():
    return (User.query.all())


def AllUsersUserID():
    return ([user.id for user in User.query.all()])


def AllUsersUserUsername():
    return ([user.username for user in User.query.all()])

# flask decorator to check if admin is logged in
def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        # get function name
        func_name = f.__name__
        print(func_name)
        CurrentUserID = int(fl.current_user.get_id()
                            ) if fl.current_user.is_authenticated else 0
        if CurrentUserID == 1:
            return f(*args, **kwargs)
        elif CurrentUserID == 0:
            flash("login to access this page", "info")
            return redirect(url_for('login')+"?next="+url_for(func_name))
        else:
            flash("login as admin to access this page", "danger")
            return redirect(url_for('login')+"?next="+url_for(func_name))
    return wrap
