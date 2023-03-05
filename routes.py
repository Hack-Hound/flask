import server_pkg.essentials as ess
from sql import DB_Manager
import imghdr
import os
from server_pkg.forms import login_form, register_form
from server_pkg.models import User
from server_pkg.app import create_app, db, login_manager, bcrypt
from flask_login import login_user, logout_user, login_required
from flask_bcrypt import check_password_hash
from werkzeug.utils import secure_filename
from werkzeug.routing import BuildError
from sqlalchemy.exc import IntegrityError, DataError, DatabaseError, InterfaceError, InvalidRequestError
import flask_login
from datetime import timedelta
from flask import render_template, redirect, flash, url_for, session, request, send_from_directory
import time
import json
from importlib.resources import path
from dataclasses import dataclass
import cv2
vid = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
# todo db mo=igration
# todo add twilio
# todo cohere
# todo add feedback table

# from flask_dropzone import Dropzone
# from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class


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

            newuser = User(
                username=username,
                email=email,
                pwd=bcrypt.generate_password_hash(pwd),
            )

            db.session.add(newuser)
            db.session.commit()
            flash(f"Account Succesfully created", "success")

        except InvalidRequestError:
            db.session.rollback()
            flash(f"Something went wrong!", "danger")
        except IntegrityError:
            db.session.rollback()
            flash(f"User already exists!.", "warning")
        except DataError:
            db.session.rollback()
            flash(f"Invalid Entry", "warning")
        except InterfaceError:
            db.session.rollback()
            flash(f"Error connecting to the database", "danger")
        except DatabaseError:
            db.session.rollback()
            flash(f"Error connecting to the database", "danger")
        except BuildError:
            db.session.rollback()
            flash(f"An error occured !", "danger")

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


@app.route("/otp", methods=["GET"], strict_slashes=False)
def otp():
    return render_template("otp.html")


@app.route("/qrcode", methods=["GET"], strict_slashes=False)
def qrcode():
    return render_template("qrcode.html")


@app.route("/readQr/")
def readQr():
    while True:
        # Capture the video frame by frame
        ret, frame = vid.read()
        data, bbox, straight_qrcode = detector.detectAndDecode(frame)
        if len(data) > 0:
            print(data)
        # Display the resulting frame
        cv2.imshow('frame', frame)
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


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


if __name__ == "__main__":
    app.run(debug=True)
