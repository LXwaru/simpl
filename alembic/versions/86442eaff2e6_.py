"""empty message

Revision ID: 86442eaff2e6
Revises: 874c8e6994f1
Create Date: 2024-09-25 15:51:30.354922

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '86442eaff2e6'
down_revision: Union[str, None] = '874c8e6994f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
