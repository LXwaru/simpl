"""empty message

Revision ID: c2e23dd73172
Revises: 24547f639129
Create Date: 2024-10-02 10:27:48.265168

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c2e23dd73172'
down_revision: Union[str, None] = '24547f639129'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
