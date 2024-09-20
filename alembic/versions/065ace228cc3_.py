"""empty message

Revision ID: 065ace228cc3
Revises: 64876ecb6b62
Create Date: 2024-09-19 15:37:56.509619

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '065ace228cc3'
down_revision: Union[str, None] = '64876ecb6b62'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
