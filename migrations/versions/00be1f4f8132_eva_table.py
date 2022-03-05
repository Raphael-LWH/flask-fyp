"""eva table

Revision ID: 00be1f4f8132
Revises: a40f50db826f
Create Date: 2020-05-06 18:38:55.663634

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00be1f4f8132'
down_revision = 'a40f50db826f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('evaluation',
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
    op.drop_table('evaluation')
    # ### end Alembic commands ###