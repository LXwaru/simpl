"""empty message

Revision ID: 049fd788827f
Revises: 02ca98239717
Create Date: 2024-11-18 15:10:47.109526

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '049fd788827f'
down_revision: Union[str, None] = '02ca98239717'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
