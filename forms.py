from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, length, Email, EqualTo


class RegisterForm(FlaskForm):
    username = StringField('username',
                           validators=[DataRequired(), length(min=2, max=10)])
    email  = StringField('email',
                         validators=[DataRequired(), Email()])
    password = PasswordField('password',
                             validators=[DataRequired(), length(min=5)])
    confirm_password = PasswordField('confirm password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create')