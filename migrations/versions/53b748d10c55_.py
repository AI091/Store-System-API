"""empty message

Revision ID: 53b748d10c55
Revises: 1ad0c291da4e
Create Date: 2022-12-07 07:31:40.290018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53b748d10c55'
down_revision = '1ad0c291da4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('manage_store',
    sa.Column('manager_id', sa.Integer(), nullable=False),
    sa.Column('store_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['manager_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['store_id'], ['stores.id'], ),
    sa.PrimaryKeyConstraint('manager_id', 'store_id')
    )
    op.drop_table('manage_stores')
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    with op.batch_alter_table('order_items', schema=None) as batch_op:
        batch_op.alter_column('unit_price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_items', schema=None) as batch_op:
        batch_op.alter_column('unit_price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    op.create_table('manage_stores',
    sa.Column('manager_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('store_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['manager_id'], ['users.id'], name='manage_stores_manager_id_fkey'),
    sa.ForeignKeyConstraint(['store_id'], ['stores.id'], name='manage_stores_store_id_fkey'),
    sa.PrimaryKeyConstraint('manager_id', 'store_id', name='manage_stores_pkey')
    )
    op.drop_table('manage_store')
    # ### end Alembic commands ###
