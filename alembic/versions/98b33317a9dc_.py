"""empty message

Revision ID: 98b33317a9dc
Revises: bc5f9e3438cc
Create Date: 2024-09-17 15:46:16.922982

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98b33317a9dc'
down_revision: Union[str, None] = 'bc5f9e3438cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
