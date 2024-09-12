"""empty message

Revision ID: 2a157bd535d4
Revises: 5c9b0099034c
Create Date: 2024-09-12 12:47:23.343599

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2a157bd535d4'
down_revision: Union[str, None] = '5c9b0099034c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
