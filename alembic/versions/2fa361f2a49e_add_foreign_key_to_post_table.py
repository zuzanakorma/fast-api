"""add foreign-key to post table

Revision ID: 2fa361f2a49e
Revises: 236d22373e27
Create Date: 2022-05-12 23:35:36.443134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fa361f2a49e'
down_revision = '236d22373e27'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", 
                          source_table="posts", 
                          referent_table="users",
                          local_cols=["owner_id"], 
                          remote_cols=["id"], 
                          ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("post", "owner_id")
    pass
