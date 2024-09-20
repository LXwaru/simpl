"""empty message

Revision ID: b5775e6c3a92
Revises: f71efcff9b10
Create Date: 2024-09-20 15:40:31.160211

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b5775e6c3a92'
down_revision: Union[str, None] = 'f71efcff9b10'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
