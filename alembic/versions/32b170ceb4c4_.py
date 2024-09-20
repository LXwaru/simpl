"""empty message

Revision ID: 32b170ceb4c4
Revises: 7e1b41111aae
Create Date: 2024-09-19 15:32:01.739353

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32b170ceb4c4'
down_revision: Union[str, None] = '7e1b41111aae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
