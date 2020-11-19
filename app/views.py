from app import app
from flask import render_template, request
from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, length, Email, EqualTo


@app.route('/')
def index():
    return render_template('main.html')

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm()
        return render_template('sign_up.html', form=form)
    return render_template('sign_up.html', form=form)

@app.route('/profile/<username>')
def antras(username):
    return render_template('profile.html')

@app.route('/page3')
def trecias():
    return render_template('page3.html')

class RegisterForm(Form):
    username = StringField('username',
                           validators=[DataRequired(), length(min=2, max=10)])
    email  = StringField('email',
                         validators=[DataRequired(), Email()])
    password = PasswordField('password',
                             validators=[DataRequired(), length(min=5)])
    confirm_password = PasswordField('confirm password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create')



