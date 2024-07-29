"""add_sendlog_table_content_colum

Revision ID: bc742869d56e
Revises: 813981f9d5cb
Create Date: 2024-07-29 15:32:59.815050

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'bc742869d56e'
down_revision: Union[str, None] = '813981f9d5cb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'send_log',
        sa.Column('event_content', sa.String(length=255), nullable=False)
    )


def downgrade() -> None:
    op.drop_column("send_log", "event_content")
