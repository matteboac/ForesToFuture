from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

#----------- ADMIN TABLE -----------
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


#----------- CONTACT TABLE -----------
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    message = db.Column(db.Text, nullable=False)


#----------- ABOUT CONTENT TABLE -----------
class AboutContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    general_objective = db.Column(db.Text, nullable=False)
    background_info = db.Column(db.Text, nullable=False)


#----------- DEFORESTATION DATA TABLE -----------
class DeforestationData(db.Model):
    __tablename__ = 'deforestation_data'
    
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    deforestation_percentage = db.Column(db.Float, nullable=False)
    forest_loss_hectares = db.Column(db.Integer)
    notes = db.Column(db.Text)
    
    __table_args__ = (
        db.UniqueConstraint('country', 'year', name='unique_country_year'),
    )


#----------- COUNTRY METADATA TABLE -----------
class CountryMetadata(db.Model):
    __tablename__ = 'country_metadata'
    
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(100), unique=True, nullable=False)
    total_forest_loss_2015_2025 = db.Column(db.Integer)
    avg_annual_loss_rate = db.Column(db.Float)
    description = db.Column(db.Text)

class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    biodiversity_records = db.relationship('BiodiversityStatus', backref='country', lazy=True)

class BiodiversityStatus(db.Model):
    __tablename__ = 'biodiversity_status'
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    affected_species = db.Column(db.Integer, nullable=False)
    ecosystem_health_index = db.Column(db.Float, nullable=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('country_id', 'year', name='unique_countries_year'),
    )