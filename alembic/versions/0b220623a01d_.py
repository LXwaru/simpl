"""empty message

Revision ID: 0b220623a01d
Revises: a55993c9ccb7
Create Date: 2024-09-12 15:43:47.303350

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0b220623a01d'
down_revision: Union[str, None] = 'a55993c9ccb7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
