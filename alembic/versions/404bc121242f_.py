"""empty message

Revision ID: 404bc121242f
Revises: 33be7e5c9abe
Create Date: 2024-09-17 15:32:13.074433

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '404bc121242f'
down_revision: Union[str, None] = '33be7e5c9abe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
