"""create posts table

Revision ID: 60359d6b96d9
Revises: 
Create Date: 2022-04-03 19:28:16.116926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60359d6b96d9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_table('posts')
    pass
