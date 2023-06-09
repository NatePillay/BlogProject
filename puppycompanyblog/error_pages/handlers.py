#handlers.py
from flask import Blueprint, render_template

error_pages = Blueprint('error_pages',__name__)


#the main approach for setting up an error handler
@error_pages.app_errorhandler(404)
def error_404(error):
    return render_template('error_pages/404.html'), 404


@error_pages.app_errorhandler(403)
def error_403(error):
    return render_template('error_pages/403.html'), 403

    #we returning a tuple (render template and actual code)
    #app_errorhandler(passin Route)
    #pass in error in function

