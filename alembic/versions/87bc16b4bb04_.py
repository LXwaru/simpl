"""empty message

Revision ID: 87bc16b4bb04
Revises: 909351c42b04
Create Date: 2024-09-20 14:15:15.209573

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '87bc16b4bb04'
down_revision: Union[str, None] = '909351c42b04'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
