"""empty message

Revision ID: 02ca98239717
Revises: b0d6ec40d365
Create Date: 2024-11-18 14:41:05.969443

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02ca98239717'
down_revision: Union[str, None] = 'b0d6ec40d365'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
