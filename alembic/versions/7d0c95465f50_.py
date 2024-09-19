"""empty message

Revision ID: 7d0c95465f50
Revises: e45e97e45ad7
Create Date: 2024-09-17 15:43:20.263979

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d0c95465f50'
down_revision: Union[str, None] = 'e45e97e45ad7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
