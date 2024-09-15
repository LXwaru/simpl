"""empty message

Revision ID: df813933bbe2
Revises: f2c1fa128a7f
Create Date: 2024-09-15 00:23:21.436997

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'df813933bbe2'
down_revision: Union[str, None] = 'f2c1fa128a7f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
