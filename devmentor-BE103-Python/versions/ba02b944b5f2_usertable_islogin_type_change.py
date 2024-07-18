"""usertable_islogin_type_change

Revision ID: ba02b944b5f2
Revises: ee5c493f0816
Create Date: 2024-07-03 16:46:54.034038

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba02b944b5f2'
down_revision: Union[str, None] = '5c22fd3d24ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('users', 'is_login',
                    existing_type=sa.String(length=255),
                    type_=sa.Boolean(),
                    existing_nullable=True,
                    nullable=False,
                    existing_server_default=None,
                    server_default=sa.text('false'))


def downgrade() -> None:
    op.alter_column('users', 'is_login',
                    existing_type=sa.Boolean(),
                    type_=sa.String(length=255),
                    existing_nullable=False,
                    nullable=True,
                    existing_server_default=sa.text('false'),
                    server_default=None)

