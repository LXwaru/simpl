"""empty message

Revision ID: 61dc5d20f30b
Revises: 394688fd7a00
Create Date: 2024-11-20 14:39:46.508914

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '61dc5d20f30b'
down_revision: Union[str, None] = '394688fd7a00'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
