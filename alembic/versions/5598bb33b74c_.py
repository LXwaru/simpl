"""empty message

Revision ID: 5598bb33b74c
Revises: 4563845082d2
Create Date: 2024-09-26 15:07:16.323837

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5598bb33b74c'
down_revision: Union[str, None] = '4563845082d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
