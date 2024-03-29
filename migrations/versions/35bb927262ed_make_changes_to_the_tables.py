"""make changes to the tables

Revision ID: 35bb927262ed
Revises: d5e4eac975ed
Create Date: 2019-11-23 22:48:06.810415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35bb927262ed'
down_revision = 'd5e4eac975ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
