import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET KEY'] = 'mysecret'


###################
## DB SETUP ##
##################
bassdir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(bassdir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db) #connect app to db


##################
#set up log in configuration #
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'user.login'


from puppycompanyblog.core.views import core
from puppycompanyblog.error_pages.handlers import error_pages
from puppycompanyblog.users.views import users

#linking views
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)

