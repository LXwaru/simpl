"""empty message

Revision ID: f71efcff9b10
Revises: 5ad089e827bc
Create Date: 2024-09-20 15:37:32.272360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f71efcff9b10'
down_revision: Union[str, None] = '5ad089e827bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
