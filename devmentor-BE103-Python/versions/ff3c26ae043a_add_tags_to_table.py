"""add tags to table

Revision ID: ff3c26ae043a
Revises: 793c63b9c188
Create Date: 2024-02-10 21:33:53.837001

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'ff3c26ae043a'
down_revision: Union[str, None] = '793c63b9c188'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",
                  sa.Column("tags", sa.String(length=255), nullable=True)
                  )
    pass


def downgrade() -> None:
    op.drop_column("posts", "tags")
    pass
