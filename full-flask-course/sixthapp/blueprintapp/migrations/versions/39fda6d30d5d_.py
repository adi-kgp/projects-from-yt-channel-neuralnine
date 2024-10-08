"""empty message

Revision ID: 39fda6d30d5d
Revises: 
Create Date: 2024-07-30 09:49:43.728276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39fda6d30d5d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('tid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('job', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('tid')
    )
    op.create_table('todos',
    sa.Column('tid', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('done', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('tid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todos')
    op.drop_table('people')
    # ### end Alembic commands ###
