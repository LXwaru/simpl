"""empty message

Revision ID: 2e7eb349c020
Revises: 59011d99afb3
Create Date: 2024-09-12 15:31:16.075093

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e7eb349c020'
down_revision: Union[str, None] = '59011d99afb3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
