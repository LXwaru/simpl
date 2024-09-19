"""empty message

Revision ID: 7ef20dc5d602
Revises: 850b16f92a0a
Create Date: 2024-09-16 15:10:40.407742

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ef20dc5d602'
down_revision: Union[str, None] = '850b16f92a0a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
