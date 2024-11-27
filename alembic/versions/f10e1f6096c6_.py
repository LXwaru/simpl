"""empty message

Revision ID: f10e1f6096c6
Revises: 705ef4040a20
Create Date: 2024-11-26 14:28:20.924640

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f10e1f6096c6'
down_revision: Union[str, None] = '705ef4040a20'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
