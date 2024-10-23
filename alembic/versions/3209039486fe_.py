"""empty message

Revision ID: 3209039486fe
Revises: 3fada82eac75
Create Date: 2024-10-21 22:41:29.733224

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3209039486fe'
down_revision: Union[str, None] = '3fada82eac75'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
