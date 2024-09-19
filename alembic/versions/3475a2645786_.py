"""empty message

Revision ID: 3475a2645786
Revises: 98b33317a9dc
Create Date: 2024-09-17 15:48:53.564643

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3475a2645786'
down_revision: Union[str, None] = '98b33317a9dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
