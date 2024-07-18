"""create_user_table

Revision ID: 61705410a563
Revises: ff3c26ae043a
Create Date: 2024-06-25 16:55:16.102866

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '61705410a563'
down_revision: Union[str, None] = 'ff3c26ae043a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_name', sa.String(length=255), nullable=False),
        sa.Column('account', sa.String(length=255), nullable=False),
        sa.Column('password', sa.String(length=255), nullable=False),
        sa.Column('is_login', sa.String(length=255), nullable=False),
        sa.Column('language', sa.String(length=255), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('users')
