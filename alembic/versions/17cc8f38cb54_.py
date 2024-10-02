"""empty message

Revision ID: 17cc8f38cb54
Revises: c2e23dd73172
Create Date: 2024-10-02 10:39:19.562345

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17cc8f38cb54'
down_revision: Union[str, None] = 'c2e23dd73172'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
