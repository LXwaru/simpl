"""empty message

Revision ID: 73038f359050
Revises: b5775e6c3a92
Create Date: 2024-09-20 15:42:35.741113

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '73038f359050'
down_revision: Union[str, None] = 'b5775e6c3a92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
