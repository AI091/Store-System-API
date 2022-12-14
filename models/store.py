from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    tags = db.relationship("TagModel", back_populates="store", lazy="dynamic")
    items = db.relationship(
        "ItemModel", back_populates="store", lazy="dynamic", passive_deletes=True
    )

    managers = db.relationship(
        "UserModel",
        back_populates="managed_stores",
        lazy="dynamic",
        secondary="manage_store",
    )
