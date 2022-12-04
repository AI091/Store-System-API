from db import db
import datetime

class CartModel(db.Model):
    __tablename__ = "carts"
    id = db.Column(db.Integer, primary_key=True)
    last_updated = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

    cart_items = db.relationship(
        "CartItemModel", back_populates="cart", passive_deletes=True
    )


class CartItemModel(db.Model):
    __tablename__ = "cart_items"
    id = db.Column(db.Integer, primary_key=True)

    item_id = db.Column(db.Integer, db.ForeignKey("items.id"), nullable=False)
    item = db.relationship("ItemModel")
    quantity = db.Column(db.Integer, nullable=False)

    cart_id = db.Column(
        db.Integer, db.ForeignKey("carts.id", ondelete="CASCADE"), nullable=False
    )
    cart = db.relationship("CartModel", back_populates="cart_items")
