"""empty message

Revision ID: bc5f9e3438cc
Revises: 7d0c95465f50
Create Date: 2024-09-17 15:44:16.193068

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc5f9e3438cc'
down_revision: Union[str, None] = '7d0c95465f50'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
