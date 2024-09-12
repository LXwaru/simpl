"""empty message

Revision ID: 59011d99afb3
Revises: 2c31cc9c5726
Create Date: 2024-09-12 15:27:15.116078

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59011d99afb3'
down_revision: Union[str, None] = '2c31cc9c5726'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
