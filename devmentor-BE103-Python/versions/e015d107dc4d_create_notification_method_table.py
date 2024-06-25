"""create_Notification_method_table

Revision ID: e015d107dc4d
Revises: 1d935ce35ed9
Create Date: 2024-06-25 21:38:39.259194

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e015d107dc4d'
down_revision: Union[str, None] = '1d935ce35ed9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'Notification_method',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('Type', sa.String(length=255), nullable=False),
        sa.Column('Data', sa.String(length=255), nullable=False),
        sa.Column('User_id', sa.Integer, sa.ForeignKey('User.id', ondelete='CASCADE'), nullable=False),
        sa.Column('Event_id', sa.Integer, sa.ForeignKey('Event.id', ondelete='CASCADE'), nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table('Notification_method')
    pass
