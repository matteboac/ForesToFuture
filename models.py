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