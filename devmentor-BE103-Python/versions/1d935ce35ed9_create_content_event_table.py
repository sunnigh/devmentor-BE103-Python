"""create_Content_Event_table

Revision ID: 1d935ce35ed9
Revises: f419a900c31e
Create Date: 2024-06-25 18:58:18.252066

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d935ce35ed9'
down_revision: Union[str, None] = 'f419a900c31e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'Content_Event',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('Language', sa.String(length=255), nullable=False),
        sa.Column('Data', sa.String(length=255), nullable=False),
        sa.Column('Event_id', sa.Integer, sa.ForeignKey('Event.id', ondelete='CASCADE'), nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table('Content_Event')
    pass
