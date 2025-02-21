"""empty message

Revision ID: 5a182e62fc84
Revises: 4984cce77ab9
Create Date: 2025-02-20 16:05:36.035387

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a182e62fc84'
down_revision: Union[str, None] = '4984cce77ab9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
