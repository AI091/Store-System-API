from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from db import db
from models import OrderModel, OrderItemModel, ItemModel, CartModel, UserModel, ACCESS
from schemas import OrderSchema

blp = Blueprint("orders", "orders", description="Operations on orders")


@blp.route("/order/<string:order_id>")
class order(MethodView):
    @blp.response(200, OrderSchema)
    @jwt_required
    def get(self, order_id):
        order = OrderModel.query.get_or_404(order_id)
        return order

    @jwt_required
    def delete(self, order_id):
        user_id = get_jwt_identity()
        if UserModel.query.get_or_404(user_id).access == ACCESS["admin"]:
            order = OrderModel.query.get_or_404(order_id)
            db.session.delete(order)
            db.session.commit()
            return {"message": "order deleted."}, 201
        else:
            return {"message": "Unauthorized delete."}, 401


@blp.route("/order")
class Neworder(MethodView):

    @blp.arguments(OrderSchema)
    @blp.response(200, OrderSchema)
    def post(self, order_data):
        order = OrderModel()
        cart = CartModel.query.get_or_404(order_data["cart_id"])
        for cart_item in cart.cart_items:
            order_item = OrderItemModel()
            order_item.item_id = cart_item.item_id
            order_item.quantity = cart_item.quantity
            order_item.unit_price = cart_item.item.price
            order_id = order.id
            db.session.add(order_item)
            db.session.commit()
        db.session.delete(cart)
        db.session.add(order)
        db.session.commit()
        return order
