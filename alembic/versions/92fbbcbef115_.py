"""empty message

Revision ID: 92fbbcbef115
Revises: 8f3697782c6f
Create Date: 2025-02-24 14:16:48.888276

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '92fbbcbef115'
down_revision: Union[str, None] = '8f3697782c6f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
