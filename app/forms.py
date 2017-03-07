from wtforms import SubmitField, StringField, validators, PasswordField
from flask_wtf import Form
from .models import User 
from flask import flash
import re

class SignupForm(Form):
    nickname = StringField("Nickname", [validators.Required("Please Enter Your Nickname")])
    email = StringField("Email",  [validators.Required("Please enter your email address.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    submit = SubmitField("Create account")

    def validate(self):
        if not Form.validate(self):
            return False
        
        user = User.query.filter_by(email = self.email.data.lower()).first()
        nick = User.query.filter_by(nickname = self.nickname.data).first()

        addresstoverify = self.email.data.lower()
        match = match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addresstoverify)

        if match == None:
            self.email.errors.append("That email doesnt looks correct")
            return False
        if user:
            self.email.errors.append("That email is already taken")
            return False
        if nick:
            self.nickname.errors.append("That nick is already taken")
            return False
        else:
            return True

class SigninForm(Form):
    email = StringField("Email", [validators.Required("Please enter your email address.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    submit = SubmitField("Sign In")

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email = self.email.data.lower()).first()
        if user and user.check_password(self.password.data):
            if user.activation_status == False:
                self.email.errors.append("Email has not been verified!")
                return False
            else:
                return True
        else:
            self.password.errors.append("Invalud e-mail or password")
            return False

class PostForm(Form):
    body = StringField("Body", [validators.Required("Body cannot be empty")])
    submit = SubmitField("Post")

    def validate(self):
        if not Form.validate(self):
            return False
        return True

class RecoveryForm(Form):
    email = StringField("Email", [validators.Required("Please enter your email address.")])
    submit = SubmitField("Send Mail")

class NewpasswordForm(Form):
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    submit = SubmitField("Reset")

    def validate(self):
        if not Form.validate(self):
            return False
        return True
