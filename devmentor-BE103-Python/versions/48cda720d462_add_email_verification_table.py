"""add email_verification_table

Revision ID: 48cda720d462
Revises: bc742869d56e
Create Date: 2024-08-26 17:26:41.805846

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = '48cda720d462'
down_revision: Union[str, None] = 'bc742869d56e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'email_verifications',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('email', sa.String(length=255), nullable=False, index=True),
        sa.Column('code', sa.String(length=6), nullable=False),
        sa.Column('expires_at', sa.DateTime, nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=func.now(), nullable=False)
    )


def downgrade():
    op.drop_table('email_verifications')
