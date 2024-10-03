"""empty message

Revision ID: 3fada82eac75
Revises: f420732ea010
Create Date: 2024-10-03 15:32:16.345289

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3fada82eac75'
down_revision: Union[str, None] = 'f420732ea010'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
