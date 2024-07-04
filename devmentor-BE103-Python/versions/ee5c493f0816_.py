"""empty message

Revision ID: ee5c493f0816
Revises: 0e57943b6c9d, 5c22fd3d24ce
Create Date: 2024-07-01 22:44:38.669186

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ee5c493f0816'
down_revision: Union[str, None] = ('0e57943b6c9d', '5c22fd3d24ce')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
