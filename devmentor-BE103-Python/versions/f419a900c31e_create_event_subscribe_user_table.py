"""create_Event_Subscribe_user_table

Revision ID: f419a900c31e
Revises: f38ae7ee3f9a
Create Date: 2024-06-25 18:49:45.600342

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f419a900c31e'
down_revision: Union[str, None] = 'f38ae7ee3f9a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'Event_Subscribe_user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('Event_id', sa.Integer, sa.ForeignKey('Event.id', ondelete='CASCADE'), nullable=False),
        sa.Column('User_id', sa.Integer, sa.ForeignKey('User.id', ondelete='CASCADE'), nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table('Event_Subscribe_user')
    pass
