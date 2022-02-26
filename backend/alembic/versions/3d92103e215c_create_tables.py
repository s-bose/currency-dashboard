"""create_tables

Revision ID: 3d92103e215c
Revises: 
Create Date: 2022-02-26 18:47:14.990590

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils import types


# revision identifiers, used by Alembic.
revision = '3d92103e215c'
down_revision = None
branch_labels = None
depends_on = None


def create_users_table() -> None:
    op.create_table(
        'users',
        sa.Column('id', types.uuid.UUIDType(), server_default=sa.text('gen_random_uuid()'), nullable=False),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('password', sa.String, nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def create_currency_table() -> None:
    op.create_table(
        'currencies',
        sa.Column('id', types.uuid.UUIDType(), server_default=sa.text('gen_random_uuid()'), nullable=False),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('country', sa.String, nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def create_portfolio_table() -> None:
    op.create_table(
        'portfolio',
        sa.Column('id', types.uuid.UUIDType(), server_default=sa.text('gen_random_uuid()'), nullable=False),
        sa.Column('user_id', types.uuid.UUIDType(), nullable=False),
        sa.Column('currency_id', types.uuid.UUIDType(), nullable=False),
        sa.Column('holdings', sa.BigInteger, nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.ForeignKeyConstraint(['currency_id'], ['currencies.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    

def upgrade():
    create_users_table()
    create_currency_table()
    create_portfolio_table()


def downgrade():
    op.drop_table('portfolio')
    op.drop_table('users')
    op.drop_table('currencies')
