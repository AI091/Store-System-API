from db import db
import datetime

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), unique=False, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80) , nullable = False)
    address = db.Column(db.String(80), nullable = False)
    birth_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime , default=datetime.datetime.utcnow )

    addresses = db.relationship('AddressModel' ,back_populates = 'user', lazy = "dynamic" , passive_deletes=True )

