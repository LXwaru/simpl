"""empty message

Revision ID: a34a2c468a76
Revises: df813933bbe2
Create Date: 2024-09-15 00:35:57.844703

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a34a2c468a76'
down_revision: Union[str, None] = 'df813933bbe2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
