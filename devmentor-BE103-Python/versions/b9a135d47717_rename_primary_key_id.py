"""rename primary key id

Revision ID: b9a135d47717
Revises: ba02b944b5f2
Create Date: 2024-07-17 12:12:15.128289

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9a135d47717'
down_revision: Union[str, None] = 'ba02b944b5f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('id', sa.Integer, primary_key=True))
    op.execute('UPDATE users SET id = user_id')
    op.drop_column('users', 'user_id')

    op.add_column('contents', sa.Column('id', sa.Integer, primary_key=True))
    op.execute('UPDATE users SET id = contents_id')
    op.drop_column('contents', 'contents_id')

    op.add_column('notify_services', sa.Column('id', sa.Integer, primary_key=True))
    op.execute('UPDATE users SET id = contents_id')
    op.drop_column('contents', 'contents_id')


def downgrade() -> None:
    op.add_column('users', sa.Column('user_id', sa.Integer, primary_key=True))
    op.execute('UPDATE users SET user_id = id')
    op.drop_column('users', 'id')

    op.add_column('contents', sa.Column('contents_id', sa.Integer, primary_key=True))
    op.execute('UPDATE users SET contents_id = id')
    op.drop_column('contents', 'id')


