"""empty message

Revision ID: 7e1b41111aae
Revises: b9c78c38d5c9
Create Date: 2024-09-19 15:30:44.200852

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7e1b41111aae'
down_revision: Union[str, None] = 'b9c78c38d5c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
