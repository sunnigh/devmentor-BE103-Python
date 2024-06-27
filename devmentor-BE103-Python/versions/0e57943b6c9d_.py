"""empty message

Revision ID: 0e57943b6c9d
Revises: ff3c26ae043a
Create Date: 2024-06-13 17:19:33.345638

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0e57943b6c9d'
down_revision: Union[str, None] = 'ff3c26ae043a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "student",  #table name
        sa.Column("student", sa.String(length=255), nullable=False),

    )
    pass


def downgrade() -> None:
    pass
