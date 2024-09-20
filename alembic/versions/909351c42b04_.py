"""empty message

Revision ID: 909351c42b04
Revises: 065ace228cc3
Create Date: 2024-09-20 14:13:38.285228

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '909351c42b04'
down_revision: Union[str, None] = '065ace228cc3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
