from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import create_access_token
from passlib.hash import pbkdf2_sha256

from db import db
from models import UserModel
from schemas import UserSchema , LoginSchema


blp = Blueprint("Users", "users", description="Operations on users")

@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self , user_data): 
        if (UserModel.query.filter(UserModel.email == user_data["email"])).first():
            abort(409 , message = "The email is already used")
        
        user = UserModel(
            email = user_data["email"] , 
            password_hash = pbkdf2_sha256.hash(user_data["password"]),
            first_name = user_data["first_name"] , 
            last_name = user_data["last_name"] , 
            phone = user_data["phone"] , 

            

        )
        db.session.add(user)
        db.session.commit()
        
        return {"message" : "User created Successfuly"} , 201 


@blp.route("/user/<int:user_id>")
class User(MethodView): 

    @blp.response(200 , UserSchema)
    def get(self , user_id): 
        user = UserModel.query.get_or_404(user_id)
        return user 
    
    def delete(self , user_id): 
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message" : "User deleted Succcessfully "} , 201


@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(LoginSchema )
    def post(self, user_data):
        user = UserModel.query.filter(
            UserModel.email == user_data["email"]
        ).first()

        if user and pbkdf2_sha256.verify(user_data["password"], user.password_hash):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}, 200

        abort(401, message="Invalid credentials.")
    

