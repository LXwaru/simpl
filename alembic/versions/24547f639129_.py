"""empty message

Revision ID: 24547f639129
Revises: 83d7272c3c25
Create Date: 2024-09-30 16:08:56.162903

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '24547f639129'
down_revision: Union[str, None] = '83d7272c3c25'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
