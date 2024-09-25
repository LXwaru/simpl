"""empty message

Revision ID: 510559e21c33
Revises: 3e3b63d72445
Create Date: 2024-09-25 14:43:30.403488

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '510559e21c33'
down_revision: Union[str, None] = '3e3b63d72445'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
