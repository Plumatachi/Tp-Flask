from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager(app)
login_manager.login_view = "login"

import os.path
def mkpath(p):
    return os.path.normpath(os.path.join(os.path.dirname(__file__), p))


from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('../myapp.db'))
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = "63f3e210-6d87-11ee-85ca-98fa9b896772"
