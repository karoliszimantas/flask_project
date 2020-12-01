from app import app
from flask import render_template, request
from forms import RegisterForm
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(8), nullable=False)
    other_data = db.relationship('AdditionalInfo', lazy=True)


class AdditionalInfo(db.Model):
    id = db.Column(db.Integer,db.ForeignKey('user.id'), primary_key=True)
    sex = db.Column(db.Boolean)



@app.route('/')
def index():
    return render_template('main.html')

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = RegisterForm()
#    if form.validate_on_submit():
    return render_template('sign_up.html', form=form)

@app.route('/profile/<username>')
def antras(username):
    return render_template('profile.html')

@app.route('/page3')
def trecias():
    return render_template('page3.html')





