"""empty message

Revision ID: f2c1fa128a7f
Revises: fb9b3e49ee51
Create Date: 2024-09-15 00:20:59.756070

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f2c1fa128a7f'
down_revision: Union[str, None] = 'fb9b3e49ee51'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
