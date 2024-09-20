"""empty message

Revision ID: cecfacc15219
Revises: 32b170ceb4c4
Create Date: 2024-09-19 15:34:35.214365

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cecfacc15219'
down_revision: Union[str, None] = '32b170ceb4c4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
