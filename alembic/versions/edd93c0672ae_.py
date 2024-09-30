"""empty message

Revision ID: edd93c0672ae
Revises: 1e9b25dc5c55
Create Date: 2024-09-27 16:10:24.086442

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'edd93c0672ae'
down_revision: Union[str, None] = '1e9b25dc5c55'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
