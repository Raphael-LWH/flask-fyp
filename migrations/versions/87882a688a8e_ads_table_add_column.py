"""ads table add column

Revision ID: 87882a688a8e
Revises: e409f0f155ea
Create Date: 2020-05-16 22:17:38.175574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87882a688a8e'
down_revision = 'e409f0f155ea'
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
