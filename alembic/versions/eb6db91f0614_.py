"""empty message

Revision ID: eb6db91f0614
Revises: cf8ec02aeadc
Create Date: 2024-09-12 16:27:35.410358

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eb6db91f0614'
down_revision: Union[str, None] = 'cf8ec02aeadc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
