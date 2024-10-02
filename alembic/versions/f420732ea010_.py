"""empty message

Revision ID: f420732ea010
Revises: fb2374401bf7
Create Date: 2024-10-02 15:37:42.998052

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f420732ea010'
down_revision: Union[str, None] = 'fb2374401bf7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
