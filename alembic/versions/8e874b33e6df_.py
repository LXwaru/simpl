"""empty message

Revision ID: 8e874b33e6df
Revises: 510559e21c33
Create Date: 2024-09-25 14:45:17.713823

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e874b33e6df'
down_revision: Union[str, None] = '510559e21c33'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
