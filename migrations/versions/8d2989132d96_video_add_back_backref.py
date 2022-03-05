"""video add back backref

Revision ID: 8d2989132d96
Revises: a4cf499cd535
Create Date: 2020-05-15 03:10:10.205113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d2989132d96'
down_revision = 'a4cf499cd535'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'news', ['picture'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'news', type_='unique')
    # ### end Alembic commands ###