"""empty message

Revision ID: abc30a0a74ef
Revises: 17cc8f38cb54
Create Date: 2024-10-02 10:43:33.595019

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'abc30a0a74ef'
down_revision: Union[str, None] = '17cc8f38cb54'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
