from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Incident(db.Model):
    __tablename__ = 'incident'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False, unique=True)
    address = db.Column(db.String(50), nullable=False)

class Detailes(db.Model):
    __tablename__ = 'detailes'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    key = db.Column(db.String(100), nullable=False)
    
def create_models(app):
    with app.app_context():
        db.create_all()