"""empty message

Revision ID: 874c8e6994f1
Revises: 8e874b33e6df
Create Date: 2024-09-25 14:46:23.844511

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '874c8e6994f1'
down_revision: Union[str, None] = '8e874b33e6df'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
