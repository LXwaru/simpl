"""empty message

Revision ID: 705ef4040a20
Revises: 61dc5d20f30b
Create Date: 2024-11-21 16:48:39.337220

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '705ef4040a20'
down_revision: Union[str, None] = '61dc5d20f30b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
