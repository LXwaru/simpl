"""empty message

Revision ID: b8056a227cfb
Revises: 28aac44049a4
Create Date: 2024-10-02 14:59:36.500512

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8056a227cfb'
down_revision: Union[str, None] = '28aac44049a4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
