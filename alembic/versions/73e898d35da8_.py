"""empty message

Revision ID: 73e898d35da8
Revises: 5598bb33b74c
Create Date: 2024-09-27 15:55:40.220431

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '73e898d35da8'
down_revision: Union[str, None] = '5598bb33b74c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
