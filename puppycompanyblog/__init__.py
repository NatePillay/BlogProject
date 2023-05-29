from flask import Flask
app = Flask(__name__)



from puppycompanyblog.core.views import core
from puppycompanyblog.error_pages.handlers import error_pages


#linking views
app.register_blueprint(core)
app.register_blueprint(error_pages)

