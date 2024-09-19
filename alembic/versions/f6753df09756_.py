"""empty message

Revision ID: f6753df09756
Revises: 9ef9b4f043b7
Create Date: 2024-09-16 15:05:40.624883

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6753df09756'
down_revision: Union[str, None] = '9ef9b4f043b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
