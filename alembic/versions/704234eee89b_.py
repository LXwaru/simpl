"""empty message

Revision ID: 704234eee89b
Revises: 7e25a2554743
Create Date: 2024-09-19 14:36:29.570766

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '704234eee89b'
down_revision: Union[str, None] = '7e25a2554743'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
