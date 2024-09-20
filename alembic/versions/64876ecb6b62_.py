"""empty message

Revision ID: 64876ecb6b62
Revises: cecfacc15219
Create Date: 2024-09-19 15:35:34.022945

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '64876ecb6b62'
down_revision: Union[str, None] = 'cecfacc15219'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
