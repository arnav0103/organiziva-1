import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_socketio import SocketIO

################

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jsoggfhxqxzisa:2b78d9f278c306075010f3d524a503f59e8191e145f4522238bde00d4f638b26@ec2-54-83-157-174.compute-1.amazonaws.com:5432/d5p553tfqa95h7'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecret'
db = SQLAlchemy(app)
Migrate(app,db)

socketio = SocketIO(app)

########### * login config * #################

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'login'
