"""add_sendlog_table

Revision ID: 813981f9d5cb
Revises: ff7c31d399b7
Create Date: 2024-07-26 17:03:32.342772

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '813981f9d5cb'
down_revision: Union[str, None] = 'ff7c31d399b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'send_log',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('event_id', sa.String(length=255), nullable=False),
        sa.Column('user_id', sa.String(length=255), nullable=False),
        sa.Column('notification_method', sa.String(length=255), nullable=False),
        sa.Column('date', sa.String(length=255), nullable=False),

    )


def downgrade() -> None:
    op.drop_table("send_log")
