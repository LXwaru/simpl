"""empty message

Revision ID: bce49e7fd7c5
Revises: 9aa3aff2f8fc
Create Date: 2025-02-21 12:13:51.898547

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bce49e7fd7c5'
down_revision: Union[str, None] = '9aa3aff2f8fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
