"""ER-model

Revision ID: 9acd4d5487a6
Revises: ff3c26ae043a
Create Date: 2024-06-24 00:50:28.292162

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9acd4d5487a6'
down_revision: Union[str, None] = 'ff3c26ae043a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'User',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('Username', sa.String(length=255), nullable=False),
        sa.Column('Account', sa.String(length=255), nullable=False),
        sa.Column('Password', sa.String(length=255), nullable=False),
        sa.Column('Is_login', sa.String(length=255), nullable=False),
        sa.Column('Language', sa.String(length=255), nullable=False)
    )

    op.create_table(
        'Event',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('Date', sa.Date, nullable=False)
    )

    op.create_table(
        'Event_Subscribe_user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('Event_id', sa.Integer, sa.ForeignKey('Event.id',ondelete='CASCADE'), nullable=False),
        sa.Column('User_id', sa.Integer, sa.ForeignKey('User.id',ondelete='CASCADE'), nullable=False)
    )

    op.create_table(
        'Content_Event',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('Language', sa.String(length=255), nullable=False),
        sa.Column('Data', sa.String(length=255), nullable=False),
        sa.Column('Event_id', sa.Integer, sa.ForeignKey('Event.id',ondelete='CASCADE'), nullable=False)
    )

    op.create_table(
        'Notification_method',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('Type', sa.String(length=255), nullable=False),
        sa.Column('Data', sa.String(length=255), nullable=False),
        sa.Column('User_id', sa.Integer, sa.ForeignKey('User.id',ondelete='CASCADE'), nullable=False),
        sa.Column('Event_id', sa.Integer, sa.ForeignKey('Event.id',ondelete='CASCADE'), nullable=False)
    )

    op.create_table(
        'Event_Notification_method',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('Event_id', sa.Integer, sa.ForeignKey('Event.id',ondelete='CASCADE'), nullable=False),
        sa.Column('Notification_method_id', sa.Integer, sa.ForeignKey('Notification_method.id',ondelete='CASCADE'), nullable=False)
    )

    pass


def downgrade() -> None:
    op.drop_table('Event_Notification_method')
    op.drop_table('Notification_method')
    op.drop_table('Content_Event')
    op.drop_table('Event_Subscribe_user')
    op.drop_table('Event')
    op.drop_table('User')
    pass
