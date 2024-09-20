"""empty message

Revision ID: 7e25a2554743
Revises: d8e7682d3dc2
Create Date: 2024-09-19 14:31:17.038670

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7e25a2554743'
down_revision: Union[str, None] = 'd8e7682d3dc2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
