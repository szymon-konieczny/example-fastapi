"""add content column to post table

Revision ID: 619ccd5e3c5b
Revises: 60359d6b96d9
Create Date: 2022-04-03 19:44:28.718578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '619ccd5e3c5b'
down_revision = '60359d6b96d9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
