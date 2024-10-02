"""empty message

Revision ID: fb2374401bf7
Revises: b8056a227cfb
Create Date: 2024-10-02 15:05:57.904621

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb2374401bf7'
down_revision: Union[str, None] = 'b8056a227cfb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
