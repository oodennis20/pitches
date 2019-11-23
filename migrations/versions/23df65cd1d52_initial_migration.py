"""Initial Migration

Revision ID: 23df65cd1d52
Revises: b533c364af92
Create Date: 2019-11-23 16:19:23.157874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23df65cd1d52'
down_revision = 'b533c364af92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_secure', sa.String(length=250), nullable=True))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(length=250), autoincrement=False, nullable=True))
    op.drop_column('users', 'password_secure')
    # ### end Alembic commands ###