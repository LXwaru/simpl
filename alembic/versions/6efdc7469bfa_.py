"""empty message

Revision ID: 6efdc7469bfa
Revises: 0b220623a01d
Create Date: 2024-09-12 16:22:04.539213

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6efdc7469bfa'
down_revision: Union[str, None] = '0b220623a01d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
