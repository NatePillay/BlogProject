from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from puppycompanyblog import db #in init.py grab slqalchemy db
from puppycompanyblog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from puppycompanyblog.users.picture_handler import add_profile_pic


users = Blueprint('users', __name__)

#register
@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    #user object created below
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.email.data
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration!') #if form valid on submission we flash this
        return redirect(url_for('user-login'))
    
    return render_template('register.html', form=form)


#login
@users.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Log in Success!')
            next = request.args.get('next')
            if next ==None or not next[0]=='/':
                next = url_for('core.index')
            return redirect(next)
    return render_template('login.html', form=form)        

#logout
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("core.index"))


#account
#user list of blog posts