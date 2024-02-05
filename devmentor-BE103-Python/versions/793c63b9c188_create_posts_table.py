"""create posts table

Revision ID: 793c63b9c188
Revises: 
Create Date: 2024-02-06 00:25:14.898798

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '793c63b9c188'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("content", sa.String(length=255), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
