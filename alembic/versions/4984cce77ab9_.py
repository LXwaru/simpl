"""empty message

Revision ID: 4984cce77ab9
Revises: 1ccbc7957d84
Create Date: 2025-02-20 16:01:21.100321

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4984cce77ab9'
down_revision: Union[str, None] = '1ccbc7957d84'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
