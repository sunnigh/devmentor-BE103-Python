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
        'notification_methods',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('type', sa.String(length=255), nullable=False),
        sa.Column('data', sa.String(length=255), nullable=False),
        sa.Column('user_id', sa.Integer,  nullable=False),
        sa.Column('event_id', sa.Integer,  nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table('notification_methods')
    pass
