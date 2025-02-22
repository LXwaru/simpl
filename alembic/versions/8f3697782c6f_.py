"""empty message

Revision ID: 8f3697782c6f
Revises: 54ac789afccb
Create Date: 2025-02-21 21:56:53.036557

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8f3697782c6f'
down_revision: Union[str, None] = '54ac789afccb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
