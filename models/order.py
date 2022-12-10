from db import db
import datetime


class OrderModel(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    customer_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    customer = db.relationship("UserModel", back_populates="orders")


class OrderItemModel(db.Model):
    __tablename__ = "order_items"

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float(precision=2), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    item = db.relationship("ItemModel")
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    order = db.relationship("OrderModel", back_populates="order_items")
