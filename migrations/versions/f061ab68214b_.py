"""empty message

Revision ID: f061ab68214b
Revises: 216c7dbe8b7c
Create Date: 2023-07-28 15:03:21.749378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f061ab68214b'
down_revision = '216c7dbe8b7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('visits', schema=None) as batch_op:
        batch_op.drop_column('visited')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('visits', schema=None) as batch_op:
        batch_op.add_column(sa.Column('visited', sa.BOOLEAN(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
