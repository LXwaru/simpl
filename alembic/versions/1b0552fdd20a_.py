"""empty message

Revision ID: 1b0552fdd20a
Revises: 86442eaff2e6
Create Date: 2024-09-25 15:57:32.456180

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b0552fdd20a'
down_revision: Union[str, None] = '86442eaff2e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
