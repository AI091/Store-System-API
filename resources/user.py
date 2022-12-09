from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from passlib.hash import pbkdf2_sha256

from db import db
from models import UserModel
from schemas import UserSchema, LoginSchema

from models import ACCESS

blp = Blueprint("Users", "users", description="Operations on users")


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if (UserModel.query.filter(UserModel.email == user_data["email"])).first():
            abort(409, message="The email is already used")

        user_data["password"] = pbkdf2_sha256.hash(user_data["password"])
        user = UserModel(**user_data)
        db.session.add(user)
        db.session.commit()

        return {"message": "User created Successfuly"}, 201


@blp.route("/user/<int:user_id>")
class User(MethodView):
    @jwt_required()
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    @jwt_required()
    def delete(self, user_id):
        current_user = get_jwt_identity()
        user = UserModel.query.get_or_404(user_id)
        if current_user == user_id or user.access == ACCESS["admin"]:
            db.session.delete(user)
            db.session.commit()
            return {"message": "User deleted Succcessfully "}, 201
        else:
            return {"message": "Unotherized delete operation"}, 401


@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(LoginSchema)
    def post(self, user_data):
        user = UserModel.query.filter(
            UserModel.email == user_data["email"]).first()

        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}, 200

        abort(401, message="Invalid credentials.")
