from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app.database import db


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def __init__(self, name, email, password, phone, role):
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.phone = phone
        self.role = role

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def find_by_username(name):
        return User.query.filter_by(name=name).first()
    
    @staticmethod
    def find_by_email(email):
        return User.query.filter_by(email=email).first()