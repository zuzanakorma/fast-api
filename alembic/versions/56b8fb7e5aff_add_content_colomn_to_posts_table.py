"""add content colomn to posts table

Revision ID: 56b8fb7e5aff
Revises: 2d00110642ac
Create Date: 2022-05-12 22:42:48.951054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56b8fb7e5aff'
down_revision = '2d00110642ac'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
