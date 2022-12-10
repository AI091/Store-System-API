from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    price = fields.Float(required=True)
    inventory = fields.Int(required=True)
    description = fields.Str(required=True)


class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class TagSchema(PlainTagSchema):
    store_id = fields.Int(load_only=True)
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    phone = fields.Str(required=True)
    access = fields.Int(required=True)


class LoginSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class CartItemSchema(Schema):
    item_id = fields.Int(required=True)
    quantity = fields.Int(required=True)


class CartSchema(Schema):
    id = fields.Int(dump_only=True)
    cart_items = fields.List(fields.Nested(CartItemSchema()), dump_only=True)


class CartUpdateSchema(Schema):
    cart_items = fields.List(fields.Nested(CartItemSchema()))


class OrderItemSchema(Schema):
    id = fields.Int(dump_only=True)
    item_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    unit_price = fields.Float(dump_only=True)


class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    cart_id = fields.Int(required=True, load_only=True)
    customer_id = fields.Int(dump_only=True)
    created_at = fields.String(dump_only=True)
    order_items = fields.List(fields.Nested(OrderItemSchema()), dump_only=True)
