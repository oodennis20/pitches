"""make changes to the tables

Revision ID: 01bb788a0aa6
Revises: 0e5d529988f8
Create Date: 2019-11-26 00:42:58.495822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01bb788a0aa6'
down_revision = '0e5d529988f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('downvotes')
    op.drop_table('upvotes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('upvotes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('upvote', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], name='upvotes_pitch_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='upvotes_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='upvotes_pkey')
    )
    op.create_table('downvotes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('downvote', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], name='downvotes_pitch_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='downvotes_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='downvotes_pkey')
    )
    # ### end Alembic commands ###
