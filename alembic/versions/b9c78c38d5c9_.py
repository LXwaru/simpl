"""empty message

Revision ID: b9c78c38d5c9
Revises: 862d4e2b234c
Create Date: 2024-09-19 15:30:06.217598

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9c78c38d5c9'
down_revision: Union[str, None] = '862d4e2b234c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
