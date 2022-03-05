"""abc fix time

Revision ID: 46ff2bd75ab1
Revises: c3bced5a0f05
Create Date: 2020-05-17 22:45:34.152871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46ff2bd75ab1'
down_revision = 'c3bced5a0f05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_news_time', table_name='news')
    op.create_unique_constraint(None, 'news', ['picture'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'news', type_='unique')
    op.create_index('ix_news_time', 'news', ['time'], unique=False)
    # ### end Alembic commands ###