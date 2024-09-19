"""empty message

Revision ID: 42a32fb94ebe
Revises: 3ec79545039e
Create Date: 2024-09-17 15:29:52.783230

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42a32fb94ebe'
down_revision: Union[str, None] = '3ec79545039e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
