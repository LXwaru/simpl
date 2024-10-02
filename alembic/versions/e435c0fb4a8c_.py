"""empty message

Revision ID: e435c0fb4a8c
Revises: e79a9b443137
Create Date: 2024-10-02 13:55:34.193440

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e435c0fb4a8c'
down_revision: Union[str, None] = 'e79a9b443137'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
