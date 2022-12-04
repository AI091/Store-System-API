from flask import Flask , jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask_admin import Admin

from flask_migrate import Migrate
from models import * 

from db import db
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.tag import blp as TagBlueprint
from resources.user import blp as UserBlueprint
from flask_admin.contrib.sqla import ModelView


import secrets

def create_app(db_url="postgresql://postgres:9871234560**@localhost/flaskapi"):
    app = Flask(__name__)
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True

    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.secret_key = 'super secret key'
    
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "secret_key"
    jwt = JWTManager(app)

    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        if identity == 1:
            return {"is_admin": True}
        return {"is_admin": False}

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)

    admin = Admin(app, name='ُُE-Commerce-API ', template_mode='bootstrap3')
    admin.add_view(ModelView(UserModel, db.session))
    admin.add_view(ModelView(ItemModel, db.session))
    admin.add_view(ModelView(StoreModel, db.session))
    admin.add_view(ModelView(TagModel, db.session))
    admin.add_view(ModelView(CollectionModel, db.session))
    admin.add_view(ModelView(AddressModel, db.session))
    
    

    return app