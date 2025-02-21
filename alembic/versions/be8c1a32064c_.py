"""empty message

Revision ID: be8c1a32064c
Revises: bce49e7fd7c5
Create Date: 2025-02-21 13:38:25.206200

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be8c1a32064c'
down_revision: Union[str, None] = 'bce49e7fd7c5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
