from db import db
import datetime

class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(precision=2) , nullable=False)
    inventory = db.Column(db.Integer, nullable = False)

    description = db.Column(db.String)
    last_updated = db.Column(db.DateTime ,onupdate = datetime.datetime.utcnow  )


    store_id = db.Column(db.Integer, db.ForeignKey("stores.id", ondelete = "CASCADE") , nullable=False )
    store = db.relationship("StoreModel", back_populates="items")

    collection_id = db.Column(db.Integer, db.ForeignKey("collections.id"))
    collection = db.relationship("CollectionModel" , back_populates = "items")

    tags = db.relationship("TagModel", back_populates="items", secondary="items_tags")
