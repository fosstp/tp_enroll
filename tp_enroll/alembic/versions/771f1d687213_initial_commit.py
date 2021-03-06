"""initial commit

Revision ID: 771f1d687213
Revises: 
Create Date: 2018-11-20 15:23:34.276272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '771f1d687213'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('newcomer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('signup_number', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('parent_name', sa.String(length=255), nullable=True),
    sa.Column('id_number', sa.String(length=255), nullable=True),
    sa.Column('parent_id_number', sa.String(length=255), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('move_in_date', sa.Date(), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('village', sa.String(length=255), nullable=True),
    sa.Column('neighborhood', sa.String(length=255), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('note', sa.String(length=255), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('home_tel', sa.String(length=255), nullable=True),
    sa.Column('dad_tel', sa.String(length=255), nullable=True),
    sa.Column('mom_tel', sa.String(length=255), nullable=True),
    sa.Column('other_tel', sa.String(length=255), nullable=True),
    sa.Column('contact_address', sa.String(length=255), nullable=True),
    sa.Column('picture_name', sa.String(length=255), nullable=True),
    sa.Column('school_number', sa.String(length=255), nullable=True),
    sa.Column('klass', sa.String(length=255), nullable=True),
    sa.Column('class_number', sa.String(length=255), nullable=True),
    sa.Column('last_update', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id_number')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('newcomer')
    # ### end Alembic commands ###
