"""empty message

Revision ID: 850b16f92a0a
Revises: 10b7d56297a8
Create Date: 2024-09-16 15:07:17.969378

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '850b16f92a0a'
down_revision: Union[str, None] = '10b7d56297a8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
