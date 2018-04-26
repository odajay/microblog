"""empty message

Revision ID: 661b8c5a2682
Revises: a6445cfc34a5
Create Date: 2018-04-25 18:11:28.454544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '661b8c5a2682'
down_revision = 'a6445cfc34a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'followers', 'user', ['followed_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'followers', type_='foreignkey')
    # ### end Alembic commands ###
