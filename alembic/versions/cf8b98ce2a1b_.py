"""empty message

Revision ID: cf8b98ce2a1b
Revises: eb6db91f0614
Create Date: 2024-09-12 22:42:59.611804

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cf8b98ce2a1b'
down_revision: Union[str, None] = 'eb6db91f0614'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
