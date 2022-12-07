from db import db
import datetime

ACCESS = {
    "user": 1,
    "store_manager": 2,
    "admin": 3,
}


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), unique=False, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    acces = db.Column(db.Integer, default=ACCESS["user"])

    addresses = db.relationship(
        "AddressModel", back_populates="user", lazy="dynamic", passive_deletes=True
    )
    orders = db.relationship("OrderModel", back_populates="customer", lazy="dynamic")

    managed_stores = db.relationship(
        "ManageStore", back_populates="managers", lazy="dynamic"
    )

    def is_admin(self):
        return self.access == ACCESS["admin"]

    def is_store_manager(self, store_id):
        return self.access == ACCESS["store_manager"] and self.managed_stores.filter(
            self.managed_stores.store_id == store_id
        )
