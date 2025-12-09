from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email


class AdminSignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=18)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    submit = SubmitField('Sign Up')


class AdminLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class AboutContentForm(FlaskForm):
    general_objective = TextAreaField('General Objective', validators=[DataRequired()])
    background_info = TextAreaField('Background Information', validators=[DataRequired()])
    submit = SubmitField('Update Content')


class ContactForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Send Message')