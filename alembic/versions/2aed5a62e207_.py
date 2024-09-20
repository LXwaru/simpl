"""empty message

Revision ID: 2aed5a62e207
Revises: 73038f359050
Create Date: 2024-09-20 15:42:46.861751

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2aed5a62e207'
down_revision: Union[str, None] = '73038f359050'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
