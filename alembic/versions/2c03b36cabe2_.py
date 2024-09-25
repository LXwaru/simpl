"""empty message

Revision ID: 2c03b36cabe2
Revises: 2aed5a62e207
Create Date: 2024-09-23 14:00:05.191901

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c03b36cabe2'
down_revision: Union[str, None] = '2aed5a62e207'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
