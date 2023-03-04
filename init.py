from server_pkg.app import create_app,db
from flask_migrate import upgrade,migrate,init,stamp
from server_pkg.models import User
from server_pkg.app import bcrypt
from sql import DB_Manager
import os

def deploy():
	"""Run deployment tasks."""
	app = create_app()
	app.app_context().push()
	db.create_all()

	# migrate database to latest revision
	init()
	stamp()
	migrate()
	upgrade()
	
deploy()
	


def init_admin():
	email = input("Enter email for admin\t: ")
	pwd = input("Enter password for admin\t: ")
	username = "admin"

	Admin = User(
		username=username,
		email=email,
		pwd=bcrypt.generate_password_hash(pwd)
	)

	db.session.add(Admin)
	db.session.commit()

init_admin()

def init_db():
	DB_Manager().TableCreation()
	arr = [
		["Item 1", 100, "Description 1"],
		["Item 2", 100, "Description 1"],
		["Item 3", 100, "Description 1"],
		["Item 4", 100, "Description 1"],
		["Item 5", 100, "Description 1"],
		["Item 6", 100, "Description 1"]]
	
	for i in range(len(arr)):
		DB_Manager().AddItem(arr[i][0],arr[i][1],arr[i][2])

init_db()
