"""empty message

Revision ID: 14a64fdf1626
Revises: a34a2c468a76
Create Date: 2024-09-15 16:29:31.006485

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14a64fdf1626'
down_revision: Union[str, None] = 'a34a2c468a76'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
