"""empty message

Revision ID: a7c7087ace92
Revises: c685a853324b
Create Date: 2024-10-21 23:59:48.799022

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a7c7087ace92'
down_revision: Union[str, None] = 'c685a853324b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
