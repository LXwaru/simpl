"""empty message

Revision ID: 2c31cc9c5726
Revises: 3af81873069d
Create Date: 2024-09-12 15:17:57.604459

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c31cc9c5726'
down_revision: Union[str, None] = '3af81873069d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
