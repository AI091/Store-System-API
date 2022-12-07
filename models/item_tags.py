from db import db


class ItemsTags(db.Model):
    __tablename__ = "items_tags"

    item_id = db.Column(db.Integer, db.ForeignKey("items.id"), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"), primary_key=True)
