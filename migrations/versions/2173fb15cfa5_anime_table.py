"""anime table

Revision ID: 2173fb15cfa5
Revises: 9300ddd12491
Create Date: 2020-05-06 00:09:12.693764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2173fb15cfa5'
down_revision = '9300ddd12491'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('anime',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('picture_name', sa.String(length=50), nullable=True),
    sa.Column('st_cat', sa.String(length=50), nullable=True),
    sa.Column('nd_cat', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['picture_name'], ['news.picture'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(None, 'news', ['picture'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'news', type_='unique')
    op.drop_table('anime')
    # ### end Alembic commands ###
