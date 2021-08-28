from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import data_required, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[data_required(), Length(min=2, max=20)])
    email = StringField("Email", validators=[data_required(), Email()])
    password = PasswordField("Password", validators=[data_required()])
    confirm_password = PasswordField("Confirm Password", validators=[data_required(), EqualTo("password")])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email is already taken')

class LoginForm(FlaskForm):
    email = StringField("email", validators=[data_required(), Email()])
    password = PasswordField("Password", validators=[data_required()])
    remember= BooleanField("Remember me")
    submit = SubmitField("Login")
