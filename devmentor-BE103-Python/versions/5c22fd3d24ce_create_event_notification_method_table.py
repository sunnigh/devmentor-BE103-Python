"""create_Event_Notification_method_table

Revision ID: 5c22fd3d24ce
Revises: e015d107dc4d
Create Date: 2024-06-25 21:42:20.857157

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5c22fd3d24ce'
down_revision: Union[str, None] = 'e015d107dc4d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'Event_Notification_method',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('Event_id', sa.Integer, sa.ForeignKey('Event.id', ondelete='CASCADE'), nullable=False),
        sa.Column('Notification_method_id', sa.Integer, sa.ForeignKey('Notification_method.id', ondelete='CASCADE'),
                  nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table('Event_Notification_method')
    pass
