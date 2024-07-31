"""rm event_id(FK)_in_notification_method

Revision ID: ff7c31d399b7
Revises: ba02b944b5f2
Create Date: 2024-07-19 14:03:35.467539

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff7c31d399b7'
down_revision: Union[str, None] = 'ba02b944b5f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("notification_methods", "event_id")


def downgrade() -> None:
    op.add_column("notification_methods",
                  sa.Column("event_id", sa.Integer, nullable=False)
                  )
