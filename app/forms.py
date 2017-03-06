from wtforms import SubmitField, StringField, validators, PasswordField
from flask_wtf import Form
from .models import User 
from flask import flash

class SignupForm(Form):
    nickname = StringField("Nickname", [validators.Required("Please Enter Your Nickname")])
    email = StringField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    submit = SubmitField("Create account")

    def validate(self):
        if not Form.validate(self):
            return False
        
        user = User.query.filter_by(email = self.email.data.lower()).first()
        nick = User.query.filter_by(nickname = self.nickname.data.lower()).first()
        if user:
            self.email.errors.append("That email is already taken")
            return False
        if nick:
            self.nickname.errors.append("That nick is already taken")
            return False
        else:
            return True

class SigninForm(Form):
    email = StringField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    submit = SubmitField("Sign In")

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email = self.email.data.lower()).first()
        if user and user.check_password(self.password.data):
            return True
        else:
            self.password.errors.append("Invalud e-mail or password")
            return False
