"""update user oush

Revision ID: 46911fd41746
Revises: 7e4037b45bca
Create Date: 2019-06-27 22:18:55.664275

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '46911fd41746'
down_revision = '7e4037b45bca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_auth', sa.Column('access_token', sa.String(length=64), nullable=True))
    op.drop_column('user_auth', 'third_key')
    op.drop_index('name', table_name='user_base')
    op.drop_column('user_base', 'password')
    op.drop_column('user_base', 'email')
    op.drop_column('user_base', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_base', sa.Column('name', mysql.VARCHAR(length=32), nullable=True))
    op.add_column('user_base', sa.Column('email', mysql.VARCHAR(length=64), nullable=True))
    op.add_column('user_base', sa.Column('password', mysql.VARCHAR(length=255), nullable=True))
    op.create_index('name', 'user_base', ['name'], unique=True)
    op.add_column('user_auth', sa.Column('third_key', mysql.VARCHAR(length=64), nullable=True))
    op.drop_column('user_auth', 'access_token')
    # ### end Alembic commands ###