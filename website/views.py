from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return '<h1>Welcome to the Flask App!</h1>'

