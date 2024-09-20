"""empty message

Revision ID: 5ad089e827bc
Revises: 72dd79db7d36
Create Date: 2024-09-20 15:36:34.594683

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ad089e827bc'
down_revision: Union[str, None] = '72dd79db7d36'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
