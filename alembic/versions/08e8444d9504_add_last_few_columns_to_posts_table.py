"""add last few columns to posts table

Revision ID: 08e8444d9504
Revises: 2fa361f2a49e
Create Date: 2022-05-12 23:43:42.483558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08e8444d9504'
down_revision = '2fa361f2a49e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("published", sa.Boolean(), 
                                    nullable=False, 
                                    server_default='True'),)
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), 
                                    nullable=False, 
                                    server_default=sa.text("NOW()")),)
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
