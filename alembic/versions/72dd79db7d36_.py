"""empty message

Revision ID: 72dd79db7d36
Revises: 99ef044318f3
Create Date: 2024-09-20 15:35:18.707079

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '72dd79db7d36'
down_revision: Union[str, None] = '99ef044318f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
