"""create_event_table

Revision ID: f38ae7ee3f9a
Revises: 61705410a563
Create Date: 2024-06-25 17:25:45.276097

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f38ae7ee3f9a'
down_revision: Union[str, None] = '61705410a563'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'events',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('event_date', sa.Date, nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table('events')
    pass
