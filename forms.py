from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, FloatField, SelectField
from wtforms.validators import DataRequired, Length, Email, NumberRange, Optional


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


# NEW FORMS FOR DEFORESTATION DATA MANAGEMENT
class DeforestationDataForm(FlaskForm):
    country = StringField('Country', validators=[DataRequired(), Length(max=100)])
    year = IntegerField('Year', validators=[DataRequired(), NumberRange(min=2000, max=2030)])
    deforestation_percentage = FloatField('Deforestation Percentage (%)', validators=[DataRequired(), NumberRange(min=0, max=100)])
    forest_loss_hectares = IntegerField('Forest Loss (Hectares)', validators=[Optional()])
    notes = TextAreaField('Notes', validators=[Optional()])
    submit = SubmitField('Save Data')


class CountryMetadataForm(FlaskForm):
    country = StringField('Country', validators=[DataRequired(), Length(max=100)])
    total_forest_loss_2015_2025 = IntegerField('Total Forest Loss 2015-2025 (Hectares)', validators=[Optional()])
    avg_annual_loss_rate = FloatField('Average Annual Loss Rate (%)', validators=[Optional(), NumberRange(min=0, max=100)])
    description = TextAreaField('Description', validators=[Optional()])
    submit = SubmitField('Save Metadata')


# NEW FORMS FOR BIODIVERSITY DATA MANAGEMENT
class BiodiversityStatusForm(FlaskForm):
    country_name = StringField('Country', validators=[DataRequired(), Length(max=100)])
    year = IntegerField('Year', validators=[DataRequired(), NumberRange(min=2000, max=2030)])
    affected_species = IntegerField('Affected Species', validators=[DataRequired(), NumberRange(min=0)])
    ecosystem_health_index = FloatField('Ecosystem Health Index', validators=[Optional(), NumberRange(min=0, max=100)])
    submit = SubmitField('Save Data')


# NEW FORM FOR COUNTRY MANAGEMENT
class CountryForm(FlaskForm):
    name = StringField('Country Name', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Save Country')