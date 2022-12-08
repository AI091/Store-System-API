from db import db


class ManageStore(db.Model):

    __tablename__ = "manage_store"

    manager_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), primary_key=True)
