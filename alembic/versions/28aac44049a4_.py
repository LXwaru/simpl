"""empty message

Revision ID: 28aac44049a4
Revises: 275a33b5c143
Create Date: 2024-10-02 14:44:30.041042

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '28aac44049a4'
down_revision: Union[str, None] = '275a33b5c143'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
