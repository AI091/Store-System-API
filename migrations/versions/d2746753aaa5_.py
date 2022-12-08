"""empty message

Revision ID: d2746753aaa5
Revises: 4c3742c8fd16
Create Date: 2022-12-04 03:14:15.570649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d2746753aaa5"
down_revision = "4c3742c8fd16"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "orders",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "order_items",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.Column("unit_price", sa.Float(precision=2), nullable=False),
        sa.Column("item_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["item_id"],
            ["items.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("items", schema=None) as batch_op:
        batch_op.alter_column(
            "price",
            existing_type=sa.REAL(),
            type_=sa.Float(precision=2),
            existing_nullable=False,
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("items", schema=None) as batch_op:
        batch_op.alter_column(
            "price",
            existing_type=sa.Float(precision=2),
            type_=sa.REAL(),
            existing_nullable=False,
        )

    op.drop_table("order_items")
    op.drop_table("orders")
    # ### end Alembic commands ###
