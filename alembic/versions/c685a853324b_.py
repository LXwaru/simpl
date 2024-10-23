"""empty message

Revision ID: c685a853324b
Revises: 3209039486fe
Create Date: 2024-10-21 23:00:55.842366

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c685a853324b'
down_revision: Union[str, None] = '3209039486fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
