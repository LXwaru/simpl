"""empty message

Revision ID: 3e3b63d72445
Revises: 2e9628cfa245
Create Date: 2024-09-23 14:30:35.855573

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e3b63d72445'
down_revision: Union[str, None] = '2e9628cfa245'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
