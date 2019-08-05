"""update userbase

Revision ID: 6250c5526eb6
Revises: 46911fd41746
Create Date: 2019-06-30 21:46:14.629955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6250c5526eb6'
down_revision = '46911fd41746'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'user_auth', 'user_base', ['uid'], ['id'])
    op.add_column('user_base', sa.Column('city', sa.String(length=16), nullable=True))
    op.add_column('user_base', sa.Column('company', sa.String(length=32), nullable=True))
    op.add_column('user_base', sa.Column('description', sa.String(length=255), nullable=True))
    op.add_column('user_base', sa.Column('email', sa.String(length=64), nullable=True))
    op.add_column('user_base', sa.Column('gender', sa.SmallInteger(), nullable=True))
    op.add_column('user_base', sa.Column('name', sa.String(length=64), nullable=True))
    op.add_column('user_base', sa.Column('password', sa.String(length=255), nullable=True))
    op.add_column('user_base', sa.Column('phone', sa.String(length=11), nullable=True))
    op.add_column('user_base', sa.Column('signature', sa.String(length=255), nullable=True))
    op.add_column('user_base', sa.Column('title', sa.String(length=32), nullable=True))
    op.add_column('user_base', sa.Column('username', sa.String(length=64), nullable=True))
    op.add_column('user_base', sa.Column('website', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_base', 'website')
    op.drop_column('user_base', 'username')
    op.drop_column('user_base', 'title')
    op.drop_column('user_base', 'signature')
    op.drop_column('user_base', 'phone')
    op.drop_column('user_base', 'password')
    op.drop_column('user_base', 'name')
    op.drop_column('user_base', 'gender')
    op.drop_column('user_base', 'email')
    op.drop_column('user_base', 'description')
    op.drop_column('user_base', 'company')
    op.drop_column('user_base', 'city')
    op.drop_constraint(None, 'user_auth', type_='foreignkey')
    # ### end Alembic commands ###
