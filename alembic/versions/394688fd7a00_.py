"""empty message

Revision ID: 394688fd7a00
Revises: e2152abbd470
Create Date: 2024-11-19 14:50:24.757123

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '394688fd7a00'
down_revision: Union[str, None] = 'e2152abbd470'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
