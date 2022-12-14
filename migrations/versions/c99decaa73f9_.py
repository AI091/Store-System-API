"""empty message

Revision ID: c99decaa73f9
Revises: f29816fcbd9d
Create Date: 2022-12-10 01:09:26.316542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c99decaa73f9'
down_revision = 'f29816fcbd9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    with op.batch_alter_table('order_items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('order_id', sa.Integer(), nullable=True))
        batch_op.alter_column('unit_price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)
        batch_op.create_foreign_key(None, 'orders', ['order_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_items', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('unit_price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.drop_column('order_id')

    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###
