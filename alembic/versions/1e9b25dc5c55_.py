"""empty message

Revision ID: 1e9b25dc5c55
Revises: 73e898d35da8
Create Date: 2024-09-27 16:07:05.614060

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e9b25dc5c55'
down_revision: Union[str, None] = '73e898d35da8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
