"""empty message

Revision ID: 4b25593ca12e
Revises: 073674c8f083
Create Date: 2018-04-25 18:19:35.248206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b25593ca12e'
down_revision = '073674c8f083'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'idtest')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('idtest', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###
