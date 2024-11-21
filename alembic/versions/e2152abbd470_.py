"""empty message

Revision ID: e2152abbd470
Revises: 049fd788827f
Create Date: 2024-11-19 14:46:44.174095

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2152abbd470'
down_revision: Union[str, None] = '049fd788827f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
