"""empty message

Revision ID: e79a9b443137
Revises: abc30a0a74ef
Create Date: 2024-10-02 10:56:38.440224

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e79a9b443137'
down_revision: Union[str, None] = 'abc30a0a74ef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
