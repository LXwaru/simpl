"""empty message

Revision ID: 54ac789afccb
Revises: be8c1a32064c
Create Date: 2025-02-21 21:53:55.459625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54ac789afccb'
down_revision: Union[str, None] = 'be8c1a32064c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
