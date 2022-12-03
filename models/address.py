from db import db 

class AddressModel(db.Model): 
    __tablename__ = "addresses"

    street = db.Column(db.String , nullable = False)
    city = db.Column(db.String  , nullable = False)
    
    user_id = db.Column(db.Integer , db.ForeignKey('users.id', ondelete="CASCADE") , primary_key=True )
    user = db.relationship("UserModel" , back_populates = "addresses")