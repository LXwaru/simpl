"""empty message

Revision ID: 2e9628cfa245
Revises: 2c03b36cabe2
Create Date: 2024-09-23 14:01:38.610056

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e9628cfa245'
down_revision: Union[str, None] = '2c03b36cabe2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
