from app import app
from flask import render_template, request
from forms import RegisterForm


@app.route('/')
def index():
    return render_template('main.html')

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = RegisterForm()
    if form.validate_on_submit():

    return render_template('sign_up.html', form=form)

@app.route('/profile/<username>')
def antras(username):
    return render_template('profile.html')

@app.route('/page3')
def trecias():
    return render_template('page3.html')





