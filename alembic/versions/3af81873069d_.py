"""empty message

Revision ID: 3af81873069d
Revises: a04e4688d32b
Create Date: 2024-09-12 15:17:30.655874

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3af81873069d'
down_revision: Union[str, None] = 'a04e4688d32b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
