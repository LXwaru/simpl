"""empty message

Revision ID: 275a33b5c143
Revises: 408cb1e000d4
Create Date: 2024-10-02 14:34:55.555983

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '275a33b5c143'
down_revision: Union[str, None] = '408cb1e000d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
