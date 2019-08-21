"""modify post user_id to uuid

Revision ID: d0c159db56f6
Revises: 1fcc0de9c5b7
Create Date: 2019-08-21 21:57:07.944504

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd0c159db56f6'
down_revision = '1fcc0de9c5b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('uuid', sa.String(length=64), nullable=True, comment='用户UUID，该文章属于那个用户'))
    op.drop_constraint('posts_ibfk_2', 'posts', type_='foreignkey')
    op.create_foreign_key(None, 'posts', 'user_base', ['uuid'], ['uuid'])
    op.drop_column('posts', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='用户ID，该文章属于那个用户'))
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.create_foreign_key('posts_ibfk_2', 'posts', 'user_base', ['user_id'], ['id'])
    op.drop_column('posts', 'uuid')
    # ### end Alembic commands ###