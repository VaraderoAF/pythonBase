"""create car table

Revision ID: b3d67524562f
Revises: 
Create Date: 2022-02-02 01:49:37.816305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3d67524562f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), server_default='', nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_new', sa.Boolean(), server_default='FALSE', nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('car')
    # ### end Alembic commands ###