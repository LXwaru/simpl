"""empty message

Revision ID: 10b7d56297a8
Revises: f6753df09756
Create Date: 2024-09-16 15:06:56.355407

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '10b7d56297a8'
down_revision: Union[str, None] = 'f6753df09756'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
