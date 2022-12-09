from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import CartModel, CartItemModel
from schemas import CartSchema, CartUpdateSchema

blp = Blueprint("Carts", "carts", description="Operations on carts")


@blp.route("/cart/<string:cart_id>")
class Cart(MethodView):
    @blp.response(200, CartSchema)
    def get(self, cart_id):
        cart = CartModel.query.get_or_404(cart_id)
        return cart

    @blp.arguments(CartUpdateSchema)
    @blp.response(200, CartSchema)
    def put(self, cart_data, cart_id):
        cart = CartModel.query.get_or_404(cart_id)
        for item in cart_data["cart_items"]:
            print(item["item_id"], cart_id)
            cart_item = CartItemModel.query.get((item["item_id"], cart_id))
            if cart_item:
                cart_item.quantity = item["quantity"]

            else:
                cart_item = CartItemModel(**item)
                cart_item.cart_id = cart.id
                db.session.add(cart_item)
                db.session.commit()

        return cart

    def delete(self, cart_id):
        cart = CartModel.query.get_or_404(cart_id, )
        db.session.delete(cart)
        db.session.commit()
        return {"message": "cart deleted."}


@blp.route("/cart")
class NewCart(MethodView):

    @blp.arguments(CartSchema)
    @blp.response(200, CartSchema)
    def post(self, cart_data):
        cart = CartModel()
        db.session.add(cart)
        db.session.commit()
        return cart
