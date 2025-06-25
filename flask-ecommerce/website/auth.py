from flask import Flask, Blueprint


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return "This is the login page"


@auth.route('/sign-up')
def sign_up():
    return "This is the sign-up page"


