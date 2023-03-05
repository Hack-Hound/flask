import cv2
# todo db mo=igration
# todo add twilio
# todo cohere
# todo add feedback table

from dataclasses import dataclass
from importlib.resources import path
from twilio.rest import Client 
import random, string
import json
import time
from flask import render_template, redirect, flash, url_for, session, request, send_from_directory
from datetime import timedelta
import flask_login
from sqlalchemy.exc import IntegrityError, DataError, DatabaseError, InterfaceError, InvalidRequestError
from werkzeug.routing import BuildError
from werkzeug.utils import secure_filename
from flask_bcrypt import check_password_hash
from flask_login import login_user, logout_user, login_required
from server_pkg.app import create_app, db, login_manager, bcrypt
from server_pkg.models import User
from server_pkg.forms import login_form, register_form
import os
import imghdr
from sql import DB_Manager
import server_pkg.essentials as ess
# from flask_dropzone import Dropzone
# from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

account_sid = 'AC2396a508b3704642de6e6f0d20346096' 
auth_token = 'b79f835fb0d0600e0c71248b77186502' 
client = Client(account_sid, auth_token) 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


app = create_app()


@app.before_request
def session_handler():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=60)

# home page


@app.route("/", methods=("GET", "POST"), strict_slashes=False)
def index():
    return render_template("index.html")


@app.route("/drowner", methods=("GET", "POST"), strict_slashes=False)
def drowner():
    return render_template("drowner.html", items=DB_Manager().QuarryAllItem())

# user authentication


@app.route("/login", methods=("GET", "POST"), strict_slashes=False)
def login():
    loginform = login_form()
    registerform = register_form()

    if loginform.validate_on_submit():
        try:
            user = User.query.filter_by(email=loginform.email.data).first()
            if check_password_hash(user.pwd, loginform.pwd.data):
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash("Invalid Username or password!", "danger")
        except Exception as e:
            flash(e, "danger")
    if registerform.validate_on_submit():
        try:
            email = registerform.email.data
            pwd = registerform.pwd.data
            username = registerform.username.data
            phone = registerform.phone.data
            x=''.join(random.choices(string.ascii_letters + string.digits, k=5))
            print(x)
            # session['otp']=x
            # message = client.messages.create(
            #                   body=x,
            #                   from_='+15674092063',
            #                   to='+919899011495'
            #               )
            # return redirect("/otp/{0}/{1}/{2}/{3}".format(email,pwd,username,phone))
        except Exception as e:
            flash(e, "danger")
        return("ok")

    return render_template("login.html",
                           loginform=loginform,
                           registerform=registerform,
                           text="Login",
                           title="Login",
                           btn_action="Login"
                           )



@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/contact", methods=("GET", "POST"), strict_slashes=False)
def contact():
    if request.method == "POST":
        vars = request.form
        print(vars)
        # todo save response

        return("response submitted")
    return render_template("contact.html")




@app.route("/qrcode", methods=["GET"], strict_slashes=False)
def qrcode():
    return render_template("qrcode.html")


@app.route("/cart", methods=["GET"], strict_slashes=False)
@app.route("/cart/<int:src>", methods=["GET"], strict_slashes=False)
def cart(src=None):
    if src == 1:
        type = request.args.get('type')
        item_id = request.args.get('item_id')
        if type == "add":
            DB_Manager().AddToCart(ess.fl.current_user.get_id(), item_id)
        elif type == "remove":
            DB_Manager().RemoveFromCart(ess.fl.current_user.get_id(), item_id)
        elif type == "delete":
            DB_Manager().DeleteFromCart(ess.fl.current_user.get_id(), item_id)
        return render_template('cart.html', items=DB_Manager().QuarryOrderByUser_ID(ess.fl.current_user.get_id()))
    return render_template('cart.html', items=DB_Manager().QuarryOrderByUser_ID(ess.fl.current_user.get_id()))
    return("ok")


@app.route("/about", methods=["GET"], strict_slashes=False)
def about():
    return render_template('about.html')
    # return("ok")


@app.route("/checkout", methods=("GET", "POST"), strict_slashes=False)
def checkout():
    pass
    return render_template('checkout.html')

@app.route("/food_menu", methods=("GET", "POST"), strict_slashes=False)
def food_menu():
    return render_template('food_menu.html')

if __name__ == "__main__":
    app.run(debug=True)
