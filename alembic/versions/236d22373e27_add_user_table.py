"""add user table

Revision ID: 236d22373e27
Revises: 56b8fb7e5aff
Create Date: 2022-05-12 22:48:00.704611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '236d22373e27'
down_revision = '56b8fb7e5aff'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                              server_default=sa.text("now()"),
                              nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")
                    )
    pass


def downgrade():
    op.drop_table("users")
    pass
