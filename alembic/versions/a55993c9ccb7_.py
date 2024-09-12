"""empty message

Revision ID: a55993c9ccb7
Revises: 2e7eb349c020
Create Date: 2024-09-12 15:33:46.388116

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a55993c9ccb7'
down_revision: Union[str, None] = '2e7eb349c020'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
