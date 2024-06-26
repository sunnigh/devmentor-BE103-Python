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
        'notify_services',
        sa.Column('notify_service_id', sa.Integer, primary_key=True),
        sa.Column('event_id', sa.Integer, sa.ForeignKey('events.event_id', ondelete='CASCADE'), nullable=False),
        sa.Column('notification_method_id', sa.Integer, sa.ForeignKey('notification_methods.notificationmethod_id', ondelete='CASCADE'),
                  nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table('notify_services')
    pass
