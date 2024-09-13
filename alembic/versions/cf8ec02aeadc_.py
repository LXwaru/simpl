"""empty message

Revision ID: cf8ec02aeadc
Revises: 6efdc7469bfa
Create Date: 2024-09-12 16:23:52.676849

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cf8ec02aeadc'
down_revision: Union[str, None] = '6efdc7469bfa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
