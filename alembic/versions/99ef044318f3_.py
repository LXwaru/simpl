"""empty message

Revision ID: 99ef044318f3
Revises: 87bc16b4bb04
Create Date: 2024-09-20 14:16:36.883794

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99ef044318f3'
down_revision: Union[str, None] = '87bc16b4bb04'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
