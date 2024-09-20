"""empty message

Revision ID: d8e7682d3dc2
Revises: 3475a2645786
Create Date: 2024-09-19 14:11:06.910235

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8e7682d3dc2'
down_revision: Union[str, None] = '3475a2645786'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
