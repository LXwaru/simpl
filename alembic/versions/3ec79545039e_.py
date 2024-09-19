"""empty message

Revision ID: 3ec79545039e
Revises: 61fc62050abb
Create Date: 2024-09-17 14:25:40.664465

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3ec79545039e'
down_revision: Union[str, None] = '61fc62050abb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
