from app import app
from flask import render_template, request, redirect
from wtforms import Form, StringField, SubmitField, TextAreaField, PasswordField, validators


@app.route('/')
def index():
    return render_template('main.html')

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    user = RegisterForm(request.form)
    if request.method == 'POST':
        return render_template('sign_up.html', form=user)
    return render_template('sign_up.html')

@app.route('/profile/<username>')
def antras(username):
    return render_template('profile.html')

@app.route('/page3')
def trecias():
    return render_template('page3.html')

class RegisterForm(Form):
    username = StringField('username', validators=[validators.DataRequired(), validators.length(min=2, max=10)])
    email  = StringField('email', validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField('password', validators=[validators.DataRequired(), validators.length(min=5)])
    confirm_password = PasswordField('confirm password', validators=[validators.DataRequired(), validators.EqualTo('password')])



